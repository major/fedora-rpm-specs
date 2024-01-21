# Upstream doesn't make releases.  We have to check the code out of git.
%global gittag   7b5a1f0039511326aeb616afb132a5065886b9d8
%global shorttag %(cut -b -7 <<< %{gittag})
%global gitdate  20180226

Name:           coxeter
Version:        3.1
Release:        11.%{gitdate}.%{shorttag}%{?dist}
Summary:        Combinatorial aspects of Coxeter group theory

# The content is GPL-1.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
License:        GPL-1.0-or-later AND Knuth-CTAN
URL:            https://github.com/tscrim/coxeter
Source0:        %{url}/archive/%{gittag}/%{name}-%{shorttag}.tar.gz
# See https://github.com/tscrim/coxeter/pull/14
Source1:        sage.h
Source2:        sage.cpp
# Test files from the sagemath project
Source3:        test.input
Source4:        test.output.expected
# Store the runtime data in a more canonical place
Patch0:         %{name}-data.patch
# Build a shared library for use by sagemath
Patch1:         %{name}-shared.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  tex(latex)

%description
This package contains a library that enables exploration of
combinatorial issues related to Coxeter groups and Hecke algebras, with
a particular emphasis on the computation of Kazhdan-Lusztig polynomials
and related questions.

%package        devel
Summary:        Header files and library links for coxeter
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and library links for developing applications that use
the coxeter library.

%package        tools
Summary:        Coxeter command line tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
Coxeter is a program for the exploration of combinatorial issues related
to Coxeter groups and Hecke algebras, with a particular emphasis on the
computation of Kazhdan-lusztig polynomials and related questions.  It is
not a symbolic algebra system; rather, it is an interface for accessing
a direct C++ implementation of the concept of a Coxeter group.

%prep
%autosetup -p0 -n %{name}-%{gittag}
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%build
%make_build optimize=true libdir=%{_libdir}
pdflatex INTRO.tex
pdflatex INTRO.tex

%install
# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -a libcoxeter3.so* %{buildroot}%{_libdir}

# Install the header files
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -p *.h *.hpp %{buildroot}%{_includedir}/%{name}

# Install the binary
mkdir -p %{buildroot}%{_bindir}
cp -p coxeter %{buildroot}%{_bindir}

# Install the runtime data
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a coxeter_matrices headers messages %{buildroot}%{_datadir}/%{name}

%check
LD_LIBRARY_PATH=$PWD ./coxeter < test.input > test.output
if ! diff test.output.expected test.output > /dev/null; then
  echo >&2 "Error testing coxeter on test.input:"
  diff -u test.output.expected test.output
  exit 1
fi

%files
%doc INTRO.pdf README
%{_libdir}/libcoxeter3.so.0*
%{_datadir}/%{name}/

%files devel
%{_includedir}/%{name}/
%{_libdir}/libcoxeter3.so

%files tools
%{_bindir}/%{name}

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-11.20180226.7b5a1f0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 3.1-10.20180226.7b5a1f0
- Stop building for 32-bit x86

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-10.20180226.7b5a1f0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-9.20180226.7b5a1f0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Jerry James <loganjerry@gmail.com> - 3.1-8.20180226.7b5a1f0
- Convert the License tag to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-8.20180226.7b5a1f0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7.20180226.7b5a1f0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6.20180226.7b5a1f0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-5.20180226.7b5a1f0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-4.20180226.7b5a1f0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Jerry James <loganjerry@gmail.com> - 3.1-3.20180226.7b5a1f0
- Build a shared library for sagemath
- Add -devel and -tools subpackages
- Add a check script

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2.20180226.7b5a1f0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul  6 2019 Jerry James <loganjerry@gmail.com> - 3.1-1.20180226.7b5a1f0
- Initial RPM
