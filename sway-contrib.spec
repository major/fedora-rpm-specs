%global tag     1.9-rc2

Name:           sway-contrib
Version:        1.9~rc2
Release:        %autorelease
Summary:        Collection of user-contributed scripts for Sway

License:        MIT
URL:            https://github.com/OctopusET/sway-contrib
Source:         %{url}/archive/%{tag}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  scdoc

Requires:       sway
Requires:       python3dist(i3ipc)

%description
%{summary}.

%package -n     grimshot
Summary:        Helper for screenshots within sway
Requires:       grim
Requires:       jq
Requires:       slurp
Requires:       sway
Requires:       /usr/bin/wl-copy
Recommends:     /usr/bin/notify-send

%description -n grimshot
Grimshot is an easy to use screenshot tool for sway. It relies on grim,
slurp and jq to do the heavy lifting, and mostly provides an easy to use
interface.


%prep
%autosetup -n %{name}-%{tag}
%py3_shebang_fix *.py


%build
scdoc <grimshot.1.scd >grimshot.1


%install
install -D -pv -t %{buildroot}%{_libexecdir}/%{name}  *.py
install -D -pv -m0644 -t %{buildroot}%{_mandir}/man1  grimshot.1
install -D -pv -m0755 -t %{buildroot}%{_bindir}  grimshot


%files
%license LICENSE
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/*.py

%files -n grimshot
%license LICENSE
%{_bindir}/grimshot
%{_mandir}/man1/grimshot.1*


%changelog
%autochangelog
