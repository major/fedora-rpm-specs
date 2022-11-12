%global pkgname io

Name:           gap-pkg-%{pkgname}
Version:        4.8.0
Release:        1%{?dist}
Summary:        Unix I/O functionality for GAP

License:        GPL-3.0-or-later
ExclusiveArch:  aarch64 ppc64le s390x x86_64
URL:            http://gap-packages.github.io/io/
Source0:        https://github.com/gap-packages/io/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig

Requires:       gap-core%{?_isa}

%description
This GAP package provides a link to the standard UNIX I/O functionality
that is available through the C library.  This part basically consists
of functions on the GAP level that allow functions in the C library to
be called.

Built on top of this is a layer for buffered input/output which is
implemented completely in the GAP language.  It is intended to be used
by programs for which it is not necessary to have full direct access to
the operating system.

On this level, quite a few convenience functions are implemented for
interprocess communication like starting up pipelines of processes to
filter data through them and to start up processes and then communicate
with them.  There is also support for creating network connections over
TCP/IP and UDP.

Building on this, the package contains an implementation of the client
side of the HTTP protocol making it possible among other things to
access web pages from within GAP.

Another part of the package is a framework for object serialization.
That is, GAP objects can be converted into a platform-independent byte
sequence which can be stored to a file or sent over the network.  The
code takes complete care of arbitrarily self-referential data structures
like lists containing themselves as an entry.  The resulting byte
strings can be read back into GAP and the original objects are rebuilt
with exactly the same self-references.  This works for most of the
standard builtin types of GAP like numbers, permutations, polynomials,
lists, and records and can be extended to nearly arbitrary GAP objects.

%package doc
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN AND LicenseRef-Fedora-Public-Domain
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-3.0-or-later AND Knuth-CTAN AND LicenseRef-Fedora-Public-Domain AND GPL-1.0-or-later AND AGPL-3.0-only
BuildArch:      noarch
Summary:        Unix I/O for GAP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
%configure --with-gaproot=%{gap_dir}
%make_build GAP="%{_bindir}/gap --bare"
make doc GAP="%{_bindir}/gap --bare"

%install
mkdir -p %{buildroot}%{gap_dir}/pkg/%{pkgname}/doc
cp -a *.g bin example gap tst %{buildroot}%{gap_dir}/pkg/%{pkgname}
%gap_copy_docs

%check
# Cannot run the HTTP test, as there is no network access on koji builders
runtest() {
  gap -l "%{buildroot}%{gap_dir};" --bare -c 'LoadPackage("io");' $1 < /dev/null 2>&1 | tee log
  ! grep -Fq 'gap> Error' log
  rm -f log
}

export LC_ALL=C.UTF-8
pushd tst
echo Testing platform
runtest platform.g
echo Testing pickle
runtest pickle.g
echo Testing buffered
runtest buffered.g
echo Testing compression
runtest compression.g
popd

%files
%doc CHANGES README.md TODO
%license GPL LICENSE
%{gap_dir}/pkg/%{pkgname}/
%exclude %{gap_dir}/pkg/%{pkgname}/doc/
%exclude %{gap_dir}/pkg/%{pkgname}/example/

%files doc
%docdir %{gap_dir}/pkg/%{pkgname}/doc/
%docdir %{gap_dir}/pkg/%{pkgname}/example/
%{gap_dir}/pkg/%{pkgname}/doc/
%{gap_dir}/pkg/%{pkgname}/example/

%changelog
* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 4.8.0-1
- Version 4.8.0
- Use upstream's method of bootstrapping
- Clarify license of the doc subpackage

* Mon Sep 26 2022 Jerry James <loganjerry@gmail.com> - 4.7.3-1
- Version 4.7.3
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 4.7.2-4
- Convert License tag to SPDX

* Sat Jul 23 2022 Jerry James <loganjerry@gmail.com> - 4.7.2-4
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 21 2021 Jerry James <loganjerry@gmail.com> - 4.7.2-1
- Version 4.7.2

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 12 2021 Jerry James <loganjerry@gmail.com> - 4.7.1-1
- Version 4.7.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 13 2020 Jerry James <loganjerry@gmail.com> - 4.7.0-4
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Jerry James <loganjerry@gmail.com> - 4.7.0-1
- New upstream version
- Drop upstreamed -largefile patch

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 4.6.0-1
- New upstream version
- Drop upstreamed -unused patch

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 4.5.4-1
- New upstream version
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Jerry James <loganjerry@gmail.com> - 4.5.1-1
- New upstream version

* Sat Jan  6 2018 Jerry James <loganjerry@gmail.com> - 4.5.0-1
- New upstream version

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 4.4.6-1
- New upstream version

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan  7 2016 Jerry James <loganjerry@gmail.com> - 4.4.5-1
- New upstream version
- Update URLs

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 4.4.4-3
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source
- Turn test failures into build failures

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Jerry James <loganjerry@gmail.com> - 4.4.4-1
- Initial RPM
