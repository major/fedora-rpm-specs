%global date    20221019
%global commit  cbd29151d263c901ff2d7b7d6dd64af8f1ee9e23
%global forgeurl https://github.com/marijnheule/drat-trim

Name:           drat-trim
Version:        0
Summary:        Proof checker for DIMACS proofs

%forgemeta

Release:        0.20%{?dist}
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
# Drat2er wants to use drat-trim as a library, but drat-trim only provides a
# binary.  Modify the sources to provide a library.
Patch0:         %{name}-library.patch
# Drat2er and CVC4 do not want to see commentary.  Apply a patch from the
# drat2er developers to optionally make it shut up.
Patch1:         %{name}-silent.patch
# Eliminate maybe-uninitialized warnings
Patch2:         %{name}-uninit.patch

BuildRequires:  gcc
BuildRequires:  help2man

%description
The proof checker DRAT-trim can be used to check whether a
propositional formula in the DIMACS format is unsatisfiable.  Given a
propositional formula and a clausal proof, DRAT-trim validates that the
proof is a certificate of unsatisfiability of the formula.  Clausal
proofs should be in the DRAT format which is used to validate the
results of the SAT competitions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers files and library links for developing applications that use
%{name}.

%package        tools
Summary:        Command line interface to %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
This package contains a command line interface to %{name}.

%prep
%forgesetup
%autopatch -p1

%build
CFLAGS='%{build_cflags} -DLONGTYPE %{build_ldflags}'

# Build the library
gcc $CFLAGS -fPIC -shared -Wl,-h,lib%{name}.so.0 -o lib%{name}.so.0.0.0 \
  %{name}.c
ln -s lib%{name}.so.0.0.0 lib%{name}.so.0
ln -s lib%{name}.so.0 lib%{name}.so

# Build the command line interface
gcc $CFLAGS -o %{name} %{name}-main.c -L. -l%{name}
export LD_LIBRARY_PATH=$PWD

# Build the other tools
gcc $CFLAGS -o lrat-check lrat-check.c
gcc $CFLAGS -o drat-compress compress.c
gcc $CFLAGS -o drat-decompress decompress.c
gcc $CFLAGS -o drat-gapless gapless.c

# Make man page for the command line interface
help2man --version-string=%{gitdate} -N -o %{name}.1 ./%{name}

%install
# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -a lib%{name}.so* %{buildroot}%{_libdir}

# Install the header file
mkdir -p %{buildroot}%{_includedir}
cp -p %{name}.h %{buildroot}%{_includedir}

# Install the binaries
mkdir -p %{buildroot}%{_bindir}
cp -p drat-compress drat-decompress drat-gapless drat-trim lrat-check \
   %{buildroot}%{_bindir}

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p drat-trim.1 %{buildroot}%{_mandir}/man1

%check
# Do not rebuild the binaries without Fedora flags
sed -i '/make/d' run-examples

export LD_LIBRARY_PATH=$PWD
sh ./run-examples

%files
%license LICENSE
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.*

%files          devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%files          tools
%doc README.md
%{_bindir}/drat-compress
%{_bindir}/drat-decompress
%{_bindir}/drat-gapless
%{_bindir}/drat-trim
%{_bindir}/lrat-check
%{_mandir}/man1/drat-trim.1*

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 23 2022 Jerry James <loganjerry@gmail.com> - 0-0.18
- Update for drat-gapless and minor bug fixes

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul  6 2022 Jerry James <loganjerry@gmail.com> - 0-0.16.20220423git43fce1c
- Update for lrat-check print and off-by-one fixes

* Mon Mar 28 2022 Jerry James <loganjerry@gmail.com> - 0-0.15.20220212git21296ed
- Update for lrat-check fix

* Fri Jan 28 2022 Jerry James <loganjerry@gmail.com> - 0-0.14.20220104git0c02b4f
- Update for ERROR fix
- Use the %%forge macros

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20211120.09d4f74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Jerry James <loganjerry@gmail.com> - 0-0.12.20211120.09d4f74
- Update for off-by-one error fix

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20210327.cec4ebb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Jerry James <loganjerry@gmail.com> - 0-0.10.20210327.cec4ebb
- Update for warning fixes

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20200914.d13f761
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Jerry James <loganjerry@gmail.com> - 0-0.8.20200914.d13f761
- Update for proof emission from lrat-check

* Mon Aug  3 2020 Jerry James <loganjerry@gmail.com> - 0-0.7.20200605.9afad0f
- Update for comment support and expandable literal lists

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20200125.a89ef60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar  5 2020 Jerry James <loganjerry@gmail.com> - 0-0.5.20200125.a89ef60
- Update to latest git snapshot for derivation fixes

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20190702.8a7a96b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20190702.8a7a96b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Jerry James <loganjerry@gmail.com> - 0-0.2.20190702.8a7a96b
- Bug fix for sortClause

* Thu Jun  6 2019 Jerry James <loganjerry@gmail.com> - 0-0.1.20190516.e6fc615
- Initial RPM
