Name:           libsemigroups
Version:        2.6.2
Release:        1%{?dist}
Summary:        C++ library for semigroups and monoids

# libsemigroups itself is GPL-3.0-or-later.
# TextFlow is BSL-1.0.
# All other licenses are due to use of eigen3.
License:        GPL-3.0-or-later AND BSL-1.0 AND MPL-2.0 AND BSD-3-Clause AND Apache-2.0
URL:            https://libsemigroups.readthedocs.io/
Source0:        https://github.com/libsemigroups/libsemigroups/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  catch2-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  python3-devel

%description
Libsemigroups is a C++ library for semigroups and monoids; it is partly
based on "Algorithms for computing finite semigroups", "Expository
Slides", and Semigroupe 2.01 by Jean-Eric Pin.

The libsemigroups library is used in the Semigroups package for GAP.

Some of the features of Semigroupe 2.01 are not yet implemented in
libsemigroups; this is a work in progress.  Missing features include
those for:

- Green's relations, or classes
- finding a zero
- minimal ideal, principal left/right ideals, or indeed any ideals
- inverses
- local submonoids
- the kernel
- variety tests.
These will be included in a future version.

Libsemigroups performs roughly the same as Semigroupe 2.01 when there is
a known upper bound on the size of the semigroup being enumerated, and
this is used to initialize the data structures for the semigroup; see
libsemigroups::Semigroup::reserve for more details.  Note that in
Semigroupe 2.01 it is always necessary to provide such an upper bound,
but in libsemigroups it is not.

Libsemigroups also has some advantages over Semigroupe 2.01:
- there is a (hopefully) convenient C++ API, which makes it relatively
  easy to create and manipulate semigroups and monoids
- there are some multithreaded methods for semigroups and their
  congruences
- you do not have to know/guess the size of a semigroup or monoid before
  you begin
- libsemigroups supports more types of elements than Semigroupe 2.01
- it is relatively straightforward to add support for further types of
  elements and semigroups
- it is possible to enumerate a certain number of elements of a
  semigroup or monoid (say if you are looking for an element with a
  particular property), to stop, and then to start the enumeration again
  at a later point
- you can instantiate as many semigroups and monoids as you can fit in
  memory
- it is possible to add more generators after a semigroup or monoid has
  been constructed, without losing or having to recompute any
  information that was previously known
- libsemigroups contains rudimentary implementations of the Todd-Coxeter
  and Knuth-Bendix algorithms for finitely presented semigroups, which
  can also be used to compute congruences of a (not necessarily finitely
  presented) semigroup or monoid.

%package devel
Summary:        Headers files for developing with %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for developing applications that use %{name}.

%package doc
# The content is GPL-3.0-or-later.  The other licenses are due to files added
# by Sphinx:
# - searchindex.js: BSD-2-Clause
# - _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# - _static/basic.css: BSD-2-Clause
# - _static/check-solid.svg: MIT
# - _static/clipboard.min.js: MIT
# - _static/copy-button.svg: MIT
# - _static/copybutton.css: MIT
# - _static/copybutton.js: MIT
# - _static/copybutton_funcs.js: MIT
# - _static/css/badge_only.css: MIT
# - _static/css/theme.css: MIT
# - _static/doctools.js: BSD-2-Clause
# - _static/documentation_options.js: BSD-2-Clause
# - _static/file.png: BSD-2-Clause
# - _static/jquery*.js: MIT
# - _static/js/badge_only.js: MIT
# - _static/js/theme.js: MIT
# - _static/language_data.js: BSD-2-Clause
# - _static/minus.png: BSD-2-Clause
# - _static/plus.png: BSD-2-Clause
# - _static/searchtools.js: BSD-2-Clause
# - _static/underscore*.js: MIT
License:        GPL-3.0-or-later AND BSD-2-Clause AND MIT
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)

Provides:       bundled(js-jquery)
Provides:       bundled(js-underscore)

%description doc
Documentation for %{name}.

%prep
%autosetup -p1

# Unbundle catch2
rm tests/catch.hpp
ln -s %{_includedir}/catch2/catch.hpp tests

# Do not override Fedora build flags
sed -i 's/ -O3//' Makefile.am

# Regenerate configure due to patch0
autoreconf -fi .

# Relax python version dependencies
sed -i 's/==/>=/g' docs/requirements.txt

%generate_buildrequires
%pyproject_buildrequires -N docs/requirements.txt

%build
# Hpcombi is an x86-specific library that uses SSE and AVX instructions.
# It is not currently available in Fedora, and we cannot assume the
# availability of AVX in any case.
%configure --disable-silent-rules --disable-static --disable-hpcombi \
  --enable-eigen --with-external-eigen --enable-fmt --with-external-fmt

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build
%make_build doc
rst2html --no-datestamp README.rst README.html
rm docs/build/html/.buildinfo

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Do not bundle the eigen3 headers
rm -fr %{buildroot}%{_includedir}/libsemigroups/Eigen

# Do not bundle the fmt headers
rm -fr %{buildroot}%{_includedir}/libsemigroups/fmt
sed -i.orig 's,"\(fmt/[[:alnum:]]*\.h\)",<\1>,g' \
    %{buildroot}%{_includedir}/libsemigroups/report.hpp
fixtimestamp %{buildroot}%{_includedir}/libsemigroups/report.hpp

%check
LD_LIBRARY_PATH=$PWD/.libs make check

%files
%doc README.html
%license LICENSE
%{_libdir}/%{name}.so.2
%{_libdir}/%{name}.so.2.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc docs/build/html
%license LICENSE

%changelog
* Tue Feb 28 2023 Jerry James <loganjerry@gmail.com> - 2.6.2-1
- Version 2.6.2
- Drop upstreamed -pessimizing-move patch

* Sat Feb 25 2023 Jerry James <loganjerry@gmail.com> - 2.6.1-1
- Version 2.6.1
- Dynamically generate python BuildRequires
- Add -pessimizing-move patch

* Tue Feb  7 2023 Jerry James <loganjerry@gmail.com> - 2.6.0-1
- Version 2.6.0

* Wed Feb  1 2023 Jerry James <loganjerry@gmail.com> - 2.5.1-2
- Explicitly depend on catch version 2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 2.5.1-1
- Version 2.5.1

* Wed Dec  7 2022 Jerry James <loganjerry@gmail.com> - 2.4.1-1
- Version 2.4.1

* Mon Dec  5 2022 Jerry James <loganjerry@gmail.com> - 2.4.0-1
- Version 2.4.0
- Refine License tag due to closer analysis of eigen3

* Sat Oct 29 2022 Jerry James <loganjerry@gmail.com> - 2.3.2-1
- Version 2.3.2

* Tue Oct 11 2022 Jerry James <loganjerry@gmail.com> - 2.3.1-1
- Version 2.3.1
- Remove -fwrapv from the build flags

* Fri Sep 23 2022 Jerry James <loganjerry@gmail.com> - 2.2.3-1
- Version 2.2.3

* Mon Sep 12 2022 Jerry James <loganjerry@gmail.com> - 2.2.2-1
- Version 2.2.2
- Convert License tag to SPDX

* Sat Aug 13 2022 Jerry James <loganjerry@gmail.com> - 2.2.1-1
- Version 2.2.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Jerry James <loganjerry@gmail.com> - 2.2.0-2
- Rebuild for fmt 9.0.0

* Mon Jul  4 2022 Jerry James <loganjerry@gmail.com> - 2.2.0-1
- Version 2.2.0

* Fri Apr 22 2022 Jerry James <loganjerry@gmail.com> - 2.1.5-1
- Version 2.1.5

* Mon Mar  7 2022 Jerry James <loganjerry@gmail.com> - 2.1.4-1
- Version 2.1.4
- Drop all patches

* Sat Jan 22 2022 Jerry James <loganjerry@gmail.com> - 1.3.7-4
- Add -const-map-key and -boolvec patches to fix FTBFS

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Richard Shaw <hobbes1069@gmail.com> - 1.3.7-2
- Rebuild for new fmt version.

* Mon Mar  1 2021 Jerry James <loganjerry@gmail.com> - 1.3.7-1
- Version 1.3.7

* Sun Feb 21 2021 Jerry James <loganjerry@gmail.com> - 1.3.6-2
- Unbundle catch2

* Fri Feb  5 2021 Jerry James <loganjerry@gmail.com> - 1.3.6-1
- Version 1.3.6

* Fri Jan 29 2021 Jerry James <loganjerry@gmail.com> - 1.3.5-1
- Version 1.3.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Jerry James <loganjerry@gmail.com> - 1.3.2-2
- Rebuild for sphinxcontrib-bibtex 2.0

* Sat Oct  3 2020 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- Version 1.3.2

* Mon Aug 31 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-3
- Fix the eigen3-devel dependency from -devel

* Mon Aug 31 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-2
- Do not ship the eigen3 headers in -devel

* Mon Aug 31 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- Version 1.3.1
- Add -autoconf patch
- Add BR on eigen3
- Do not ship the fmt headers in -devel

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- Version 1.2.1

* Fri Jun 12 2020 Jerry James <loganjerry@gmail.com> - 1.1.0-1
- Version 1.1.0

* Tue Apr 21 2020 Jerry James <loganjerry@gmail.com> - 1.0.9-1
- Version 1.0.9

* Mon Apr 20 2020 Jerry James <loganjerry@gmail.com> - 1.0.8-1
- Version 1.0.8
- Drop upstreamed -fmt patch

* Thu Apr  9 2020 Jerry James <loganjerry@gmail.com> - 1.0.7-2
- Add -fmt patch for compatibility with fmt 6.2.0

* Sat Mar 21 2020 Jerry James <loganjerry@gmail.com> - 1.0.7-1
- Version 1.0.7
- Create font symlinks with fc-match for greater robustness

* Sun Feb  9 2020 Jerry James <loganjerry@gmail.com> - 1.0.6-1
- Version 1.0.6

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Jerry James <loganjerry@gmail.com> - 1.0.5-1
- Version 1.0.5
- Drop -unbundle-fmt patch in favor of --with-external-fmt arg to configure

* Fri Dec 13 2019 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- Version 1.0.3
- New URLs
- Drop -use-after-free patch
- Unbundle fmt

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Jerry James <loganjerry@gmail.com> - 0.6.7-1
- New upstream version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 Jerry James <loganjerry@gmail.com> - 0.6.4-1
- New upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Jerry James <loganjerry@gmail.com> - 0.6.3-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Jerry James <loganjerry@gmail.com> - 0.6.2-1
- New upstream version

* Sat Dec 30 2017 Jerry James <loganjerry@gmail.com> - 0.6.1-1
- New upstream version
- Add -use-after-free patch to fix test failures

* Tue Dec 12 2017 Jerry James <loganjerry@gmail.com> - 0.6.0-1
- New upstream version

* Sat Oct  7 2017 Jerry James <loganjerry@gmail.com> - 0.5.2-1
- New upstream version

* Sat Sep 30 2017 Jerry James <loganjerry@gmail.com> - 0.5.0-1
- New upstream version

* Mon Sep  4 2017 Jerry James <loganjerry@gmail.com> - 0.3.2-1
- New upstream version

* Sun Jul 30 2017 Jerry James <loganjerry@gmail.com> - 0.3.1-3
- Install the license with the -doc subpackage
- Make -doc noarch

* Sat Jul 29 2017 Jerry James <loganjerry@gmail.com> - 0.3.1-2
- Move documentation to a -doc subpackage
- Link with libpthread to fix an undefined non-weak symbol
- Kill the rpath

* Thu Jul 27 2017 Jerry James <loganjerry@gmail.com> - 0.3.1-1
- Initial RPM
