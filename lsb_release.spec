Name:           lsb_release
Version:        3.3
Release:        3%{?dist}
Summary:        Linux Standard Base Release Tool using os-release(5)

License:        GPL-2.0-or-later
URL:            https://github.com/thkukuk/lsb-release_os-release
Source:         %{url}/archive/v%{version}/lsb-release_os-release-%{version}.tar.gz

BuildRequires:  make
# For the modified vendored copy of help2man required to make the man page
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl(POSIX)

# Because sometimes there's just too much minimization
Requires:       /usr/bin/getopt
Requires:       /usr/bin/sed
Requires:       /usr/bin/tr

# In case people use the debian name for this package...
Provides:       lsb-release = %{version}-%{release}

# This is intended to be an alternative to the "full" redhat-lsb version
Conflicts:      redhat-lsb-core

BuildArch:      noarch

%description
Linux Standard Base Release Tool, ported to use os-release(5)
as the data source.


%prep
%autosetup -n lsb-release_os-release-%{version} -p1


%build
make


%install
make install INSTALL_ROOT=%{buildroot}%{_prefix}


%files
%license COPYING
%doc README
%{_bindir}/lsb?release
%{_mandir}/man1/lsb?release.1*


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 08 2023 Neal Gompa <ngompa@fedoraproject.org> - 3.3-1
- Update to 3.3

* Mon Oct 30 2023 Neal Gompa <ngompa@fedoraproject.org> - 3.2-2
- Add patch to support generic DISTRIB_ID guessing

* Wed Oct 25 2023 Neal Gompa <ngompa@fedoraproject.org> - 3.2-1
- Update to 3.2
- Refresh patch with upstream version

* Thu Dec 02 2021 Neal Gompa <ngompa@centosproject.org> - 3.1-2
- Patch in support for Red Hat distributions

* Thu Dec 02 2021 Neal Gompa <ngompa@centosproject.org> - 3.1-1
- Initial package
