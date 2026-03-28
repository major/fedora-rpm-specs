Name:		fedora-flathub-remote
Version:	1
Release:	%autorelease
Summary:	Third party remote pointing to a filtered version of flathub.org

License:	MIT
URL:		https://pagure.io/fedora-flathub-filter
Source0:	LICENSE
Source1:	fedora-flathub.filter
Source2:	fedora-flathub.conf
Source3:	fedora-flathub.flatpakrepo

BuildArch:	noarch

Requires:	fedora-third-party
Requires:	flatpak

%description
This package adds configuration to add a remote pointing to flathub.org when
third-party repositories are enabled on a Fedora Linux system. This remote is
filtered to include only specific Fedora-approved packages. (If the user
installs the Flathub remote manually, the filter is removed, and the flathub
remote is no longer managed as a third-party repository.)


%prep

%build

%install
install -D -m0644 %{SOURCE0} %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

install -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/flatpak/fedora-flathub.filter
install -D -m0644 %{SOURCE2} -t %{buildroot}%{_prefix}/lib/fedora-third-party/conf.d
install -D -m0644 %{SOURCE3} -t %{buildroot}%{_prefix}/lib/fedora-third-party/conf.d


%files
%license LICENSE
%{_datadir}/flatpak/fedora-flathub.filter
%{_prefix}/lib/fedora-third-party/conf.d/*


%changelog
%autochangelog
