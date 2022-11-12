%global pkgname  zeromqinterface
%global upname   ZeroMQInterface

Name:           gap-pkg-%{pkgname}
Version:        0.14
Release:        2%{?dist}
Summary:        ZeroMQ bindings for GAP

License:        GPL-2.0-or-later
ExclusiveArch:  aarch64 ppc64le s390x x86_64
URL:            https://gap-packages.github.io/ZeroMQInterface/
Source0:        https://github.com/gap-packages/ZeroMQInterface/releases/download/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  python3-devel

Requires:       gap-core%{?_isa}

%description
This package provides both low-level bindings as well as some higher
level interfaces for the ZeroMQ message passing library for GAP and
HPC-GAP, enabling lightweight distributed computation.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN AND LicenseRef-Fedora-Public-Domain
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND Knuth-CTAN AND LicenseRef-Fedora-Public-Domain AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Documentation for ZeroMQ bindings for GAP
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version}

# Fix python shebang
sed -i.orig 's,%{_bindir}/env python,%{__python3},' zgap
touch -r zgap.orig zgap
rm zgap.orig

%build
export LC_ALL=C.UTF-8
%configure --with-gaproot=%{gap_dir}
%make_build

# Build the documentation
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_dir}/pkg/%{upname}/doc
cp -a bin gap tst *.g %{buildroot}%{gap_dir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

mkdir -p %{buildroot}%{gap_dir}/bin
cp -p zgap %{buildroot}%{gap_dir}/bin

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_dir};" tst/testall.g

%files
%doc CHANGES.md README.md
%license COPYRIGHT.md LICENSE
%{gap_dir}/bin/zgap
%{gap_dir}/pkg/%{upname}/
%exclude %{gap_dir}/pkg/%{upname}/doc/

%files doc
%docdir %{gap_dir}/pkg/%{upname}/doc/
%{gap_dir}/pkg/%{upname}/doc/

%changelog
* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 0.14-2
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 0.14-2
- Update for gap 4.12.0
- Convert License tag to SPDX

* Sat Jul 30 2022 Jerry James <loganjerry@gmail.com> - 0.14-1
- Version 0.14

* Sun Jul 24 2022 Jerry James <loganjerry@gmail.com> - 0.13-5
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 14 2021 Jerry James <loganjerry@gmail.com> - 0.13-1
- Version 0.13

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 0.12-3
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov  2 2019 Jerry James <loganjerry@gmail.com> - 0.12-1
- Version 0.12

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 0.11-2
- Rebuild for changed bin dir name in gap 4.10.1

* Wed Feb 27 2019 Jerry James <loganjerry@gmail.com> - 0.11-1
- Initial RPM
