%global short_name backgrounds

Name:           fedora-eln-backgrounds
Version:        1.0
Release:        %autorelease
Summary:        Fedora ELN default desktop background

License:        CC-BY-SA-4.0
URL:            https://docs.fedoraproject.org/en-US/eln/
Source0:        https://github.com/fedora-eln/%{short_name}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  ImageMagick

%if 0%{?eln}
Provides:       system-backgrounds
%endif


%description
This package contains desktop backgrounds for the Fedora ELN default theme.


%prep
%autosetup -n %{short_name}-%{version}


%build
%make_build


%install
%make_install


%files
%license CC-BY-SA-4.0 Attribution
%dir %{_datadir}/backgrounds
%dir %{_datadir}/backgrounds/fedora-eln
%dir %{_datadir}/backgrounds/fedora-eln/default
%dir %{_datadir}/gnome-background-properties/
%{_datadir}/backgrounds/fedora-eln/default/fedora-eln*.{png,xml}
%{_datadir}/gnome-background-properties/fedora-eln.xml

%changelog
%autochangelog
