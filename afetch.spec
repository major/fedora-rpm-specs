Name:           afetch
Version:        2.2.0
Release:        4%{?dist}
Summary:        Simple system info written in C

License:        GPL-3.0-only
URL:            https://github.com/13-CF/afetch
Source0:        %{url}/archive/V%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc

# https://github.com/13-CF/afetch/pull/94
Patch:          use_our_build_flags.patch

%description
Fast and simple system info (for UNIX based operating systems)
written in POSIX compliant C99


%prep
%autosetup


%build
%if 0%{?rhel} || 0%{?fedora} < 36
%set_build_flags
%endif
%make_build


%install
%make_install PREFIX=%{_prefix}


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 21 2022 Jonathan Wright <jonathan@almalinux.org> - 2.2.0-2
- Fix spec to build on f35

* Tue Aug 16 2022 Jonathan Wright <jonathan@almalinux.org> - 2.2.0-1
- Initial package build
- rhbz#2118837
