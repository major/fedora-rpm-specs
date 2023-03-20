%global upstream_name   papirus-libreoffice-theme
%global debug_package %{nil}

Name:           libreoffice-icon-theme-papirus
Version:        20170228
Release:        %autorelease
Summary:        Papirus theme for LibreOffice

License:        GPLv3
URL:            https://github.com/PapirusDevelopmentTeam/papirus-libreoffice-theme
Source0:        %url/archive/%{version}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  make

%description
Papirus theme for LibreOffice.

It is available in three variants:

 - ePapirus
 - Papirus
 - Papirus Dark


%prep
%autosetup -n %{upstream_name}-%{version}


%build
# Nothing to build


%install
%make_install PREFIX=%{_libdir}


%files
%license LICENSE
%doc AUTHORS README.md
%dir %{_libdir}/libreoffice
%dir %{_libdir}/libreoffice/share
%dir %{_libdir}/libreoffice/share/config
%{_libdir}/libreoffice/share/config/images_*.zip


%changelog
%autochangelog
