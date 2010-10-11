Summary:	Themes for cairo-dock
Name:     	cairo-dock-themes
Version:	1.6.3.1
Release:	%mkrel 3
License:	GPLv3+
Group:		Graphical desktop/Other
Source0: 	http://download.berlios.de/cairo-dock/%name-%version.tar.bz2
Patch0:		cairo-dock-themes-1.6.3.1-theme-dir.patch
URL:		http://www.cairo-dock.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	cairo-dock-devel
Requires:	cairo-dock
BuildArch:	noarch

%description
This package contains all cairo-dock themes.

%files
%defattr(-, root, root)
%{_datadir}/cairo-dock/themes/*

#---------------------------------------------------------------------
%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT
