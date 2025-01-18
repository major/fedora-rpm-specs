Name:           createrepo-agent
Version:        0.4.2
Release:        5%{?dist}
Summary:        Rapidly and repeatedly generate RPM repository metadata

License:        Apache-2.0
URL:            https://github.com/osrf/createrepo-agent
Source0:        https://github.com/osrf/createrepo-agent/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(createrepo_c)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(libassuan)

%description
createrepo-agent is a tool for rapidly iterating on clusters of associated
RPM repositories. It leverages Assuan IPC to create a daemon process which
caches the metadata for each sub-repository in the cluster so that it
doesn't need to be re-loaded and parsed each time a change is made. The
most notable implementation of the Assuan protocol is gpg-agent, which
gives createrepo-agent its name.


%prep
%autosetup -p1


%build
%cmake
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE
%doc README.md TODO.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 23 2023 Scott K Logan <logans@cottsay.net> - 0.4.2-1
- Initial package
