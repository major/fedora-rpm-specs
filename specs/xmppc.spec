Name:           xmppc
Version:        0.1.2
Release:        9%{?dist}
Summary:        A command-line interface (CLI) XMPP Client

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://codeberg.org/Anoxinon_e.V./%{name}
Source0:        https://codeberg.org/Anoxinon_e.V./%{name}/archive/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  libstrophe-devel
BuildRequires:  glib2-devel
BuildRequires:  gpgme-devel
# For docs:
BuildRequires:  doxygen
BuildRequires:  asciidoc

%description
xmppc is a XMPP command line interface client. It's written in C and
is using the xmpp library libstrophe.



%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
The %{name}-doc package contains HTML documentation for developing
applications that use %{name}.



%prep
%autosetup -n %{name}


%build
autoreconf -i -W all
%configure
%make_build

# Build HTML documentation
pushd doc/
make  # results are in doc/doxygen/html/
popd


%install
%make_install
# Install HTML documentation for the doc subpackage
# (destination directory already exists)
cp -a doc/doxygen/html/ %{buildroot}%{_pkgdocdir}/


%check
make check



%files
%license LICENSE
%doc README.md changelog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*


%files doc
%{_pkgdocdir}/html/
%{_pkgdocdir}/%{name}.1.html



%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.2-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 23 2023 Matthieu Saulnier <fantom@fedoraproject.org> - 0.1.2-5
- Rebuild for libstrophe 0.12.3
- Improve file ownership in doc subpackage

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 15 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 0.1.2-2
- Fix Requires tag in the doc subpackage

* Wed Sep 14 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 19 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.1.0-1
- Package Review RHBZ#1996107:
  - Initial packaging
