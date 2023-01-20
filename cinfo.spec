Name:           cinfo
Version:        0.5.1
Release:        2%{?dist}
Summary:        Fast and minimal system information tool

License:        GPL-3.0-only
URL:            https://github.com/mrdotx/cinfo
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
%{summary}

%prep
%autosetup


%build
%set_build_flags
%make_build


%install
%make_install PREFIX=%{_prefix}


%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 07 2022 Jonathan Wright <jonathan@almalinux.org> 0.5.1-1
- update to 0.5.1 rhbz#2140024

* Tue Oct 11 2022 Jonathan Wright <jonathan@almalinux.org> 0.5.0-1
- update to 0.5.0 rhbz#2133897

* Tue Aug 30 2022 Jonathan Wright <jonathan@almalinux.org> 0.4.9-1
- update to 0.4.9
- rhbz#2121986

* Sat Aug 20 2022 Jonathan Wright <jonathan@almalinux.org> 0.4.8-1
- Initial package build
- rhbz#2120002
