Summary:	Themes for cairo-dock
Name:		cairo-dock-themes
Version:	1.6.3.1
Release:	6
License:	GPLv3+
Group:		Graphical desktop/Other
Source0:	http://download.berlios.de/cairo-dock/%{name}-%{version}.tar.bz2
Source1:	%{name}.rpmlintrc
Patch0:		cairo-dock-themes-1.6.3.1-theme-dir.patch
URL:		https://www.cairo-dock.org/
BuildRequires:	cairo-dock-devel
Requires:	cairo-dock
BuildArch:	noarch

%description
This package contains all cairo-dock themes.

%files
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
%makeinstall_std

