%global debug_package %{nil}

# NLR code is incompatible with Link Time Optimizations
# https://github.com/micropython/micropython/issues/8421
%global _lto_cflags %nil

# Add -Wformat as it's required along with -Wformat-security
# set by redhat-rpm-config
%global _warning_options %_warning_options -Wformat

Name:           micropython
Version:        1.19.1
Release:        4%{?dist}
Summary:        Implementation of Python 3 with very low memory footprint

# micorpython itself is MIT
# axtls and berkeley-db are BSD
License:        MIT and BSD

URL:            http://micropython.org/
Source0:        https://github.com/micropython/micropython/archive/v%{version}.tar.gz

%global axtls_commit 531cab9c278c947d268bd4c94ecab9153a961b43
Source1:       https://github.com/micropython/axtls/archive/%{axtls_commit}/axtls-%{axtls_commit}.tar.gz

%global berkley_commit 35aaec4418ad78628a3b935885dd189d41ce779b
Source2:       https://github.com/pfalcon/berkeley-db-1.xx/archive/%{berkley_commit}/berkeley-db-1.xx-%{berkley_commit}.tar.gz
Patch0:        micropython-c99.patch

# Other arches need active porting
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExclusiveArch:  %{arm} x86_64
%else
ExclusiveArch:  %{arm} %{ix86} x86_64
%endif

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  libffi-devel
BuildRequires:  readline-devel
BuildRequires:  execstack
BuildRequires:  openssl-devel

# Part of the tests runs MicroPython and CPython and compares the results.
# MicroPython is ~3.4, but the testing framework supports newer Pythons as well.
# We use the latest working CPython version in those test, setting the
# MICROPY_CPYTHON3 environment variable.
# Normal %%{pytohn3} is used anywhere else.
# There is no runtime dependency on this CPython (or any other).
%global cpython_version_tests 3.9
BuildRequires:  %{_bindir}/python%{cpython_version_tests}

Provides:       bundled(axtls) = 2.1.5
Provides:       bundled(libdb) = 1.85

%description
Implementation of Python 3 with very low memory footprint

%prep
%autosetup -p1 -n %{name}-%{version}

# git submodules
rmdir lib/axtls
tar -xf %{SOURCE1}
mv axtls-%{axtls_commit} lib/axtls

head -n 28 lib/axtls/axtlswrap/Makefile > LICENSE.axtls

rmdir lib/berkeley-db-1.xx
tar -xf %{SOURCE2}
mv berkeley-db-1.xx-%{berkley_commit} lib/berkeley-db-1.xx

head -n 32 lib/berkeley-db-1.xx/db/db.c > LICENSE.libdb

# Fix shebangs
files=$(grep -rl '#!/usr/bin/env python')
%py3_shebang_fix $files

# Removing pre-built binary; not required for build
rm ports/cc3200/bootmgr/relocator/relocator.bin

%build
# Build the cross-compiler
%make_build -C mpy-cross

# Build the unbundled submodules
%make_build -C ports/unix axtls V=1

# Build the interpreter
%make_build -C ports/unix PYTHON=%{python3} V=1

execstack -c ports/unix/micropython

%check
pushd ports/unix
export MICROPY_CPYTHON3=python%{cpython_version_tests}
make PYTHON=%{python3} V=1 test
popd

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 755 ports/unix/micropython %{buildroot}%{_bindir}

%files
%doc README.md
%license LICENSE LICENSE.axtls LICENSE.libdb
%{_bindir}/micropython

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Florian Weimer <fweimer@redhat.com> - 1.19.1-3
- Port to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Charalampos Stratakis <cstratak@redhat.com> - 1.19.1-1
- Update to 1.19.1
- Fixes: rhbz#2097936

* Fri Mar 04 2022 Charalampos Stratakis <cstratak@redhat.com> - 1.18-1
- Update to 1.18
- Disable Link Time Optimizations
- Fixes: rhbz#2046737, rhbz#2041651

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Fri Sep 03 2021 Miro Hrončok <mhroncok@redhat.com> - 1.17-1
- Update to 1.17
- Fixes: rhbz#2000869

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 24 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.16-1
- Update to 1.16

* Thu May 06 2021 Miro Hrončok <mhroncok@redhat.com> - 1.15-1
- Update to 1.15
- Fixes rhbz#1950805
- Fix build on 32bit architectures
- Fixes rhbz#1922142

* Fri Mar 19 2021 Charalampos Stratakis <cstratak@redhat.com> - 1.14-1
- Update to 1.14 (#1924346)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Tomas Hrnciar <thrnciar@redhat.com> - 1.13-1
- Update to 1.13 (#1874689)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.12-1
- Update to 1.12 (#1785781)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11-1
- Update to 1.11 (#1714903)

* Sun Feb 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10-1
- Update to 1.10 (#1669547)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.4-2
- Enable i686, fix a FTBFS (#1556924)

* Wed Aug 01 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.4-1
- Update to 1.9.4 (#1577187)
- Use CPython 3.6 in tests that compare results due to PEP479 (#1604827)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.3-5
- Rebuilt for Python 3.7

* Thu Mar 15 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.3-4
- Get rid of python2 build dependency
- Temporarily disable i686, investigate later

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Miro Hrončok <mhroncok@redhat.com> - 1.9.3-1
- Update to 1.9.3 (#1508424)

* Tue Sep 12 2017 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-1
- Update to 1.9.2 (#1332739) and fix FTBFS (#1423943)
- Add 2 git submodules to sources, add bundled provides
- Changed license tag to include BSD (becasue of those submodules)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.8.1-2
- Add ExclusiveArch, other arches need active porting

* Wed Jun 06 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.8.1-1
- Update to 1.8.1

* Wed May 04 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.8-1
- Update to 1.8

* Tue Apr 19 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.7-1
- Update to 1.7

* Tue Apr 05 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.6-3
- Remove license-encumbered bits in stmhal/

* Tue Apr 05 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.6-2
- Remove cc3200/bootmgr/relocator/relocator.bin
- Fix license macro

* Tue Apr 05 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.6-1
- Update to 1.6

* Tue May 20 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.2-1
- Initial spec
