%global gitdate 20190307
%global commit 521caf16149df3dfa46f700ec1fab56f8cc12a18
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           drat2er
Version:        0
Release:        0.14.%{gitdate}.%{shortcommit}%{?dist}
Summary:        Proof transformer for propositional logic

License:        MIT
URL:            https://github.com/alex-ozdemir/drat2er/
Source0:        https://github.com/alex-ozdemir/drat2er/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# Unbundle the third-party libraries
Patch0:         %{name}-unbundle.patch
# Build a shared library instead of a static library
Patch1:         %{name}-shared.patch
# Fix a C++ assertion failure due to calling front() on an empty string
Patch2:         %{name}-string-front.patch
# Fix drat-trim problems caused by passing arguments in the wrong order.
# Drat-trim does all actions associated with a command line argument before
# processing the next one.  Therefore, the verbosity option must come first.
Patch3:         %{name}-arg-order.patch
# CLI11 v2.0.0 changes the signature of add_option() slightly, and the final
# bool is no longer needed.
Patch4:		%{name}-cli11-2-compat.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  catch2-devel
BuildRequires:  cli11-static
BuildRequires:  cmake
BuildRequires:  drat-trim-devel
BuildRequires:  drat-trim-tools
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make

%description
Drat2er is a tool for transforming proofs that are usually produced by
SAT solvers.  It takes as input a propositional formula (specified in
the DIMACS format) together with a DRAT proof (DRAT is the current
standard format for proofs in SAT solving), and outputs an
extended-resolution proof of the formula in either the TRACECHECK or
the DRAT format.  The details of this proof transformation are
described in the paper "Extended Resolution Simulates DRAT" (IJCAR
2018).  Note that if drat2er is given as input a DRUP proof, then it
transforms this DRUP proof into an ordinary resolution proof.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers files and library links for developing applications that use
%{name}.

%package        tools
# The project itself is MIT.
# The code added by cli11 is BSD-3-Clause.
License:        MIT AND BSD-3-Clause
Summary:        Command line interface to %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
This package contains a command line interface to %{name}.

%prep
%autosetup -p0 -n %{name}-%{commit}

# Do not use the bundled libraries
rm -fr third-party

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build
export LD_LIBRARY_PATH=$PWD/%{_vpath_builddir}/%{_lib}
help2man --version-string=%{gitdate} -N -o %{name}.1 \
  %{_vpath_builddir}/bin/%{name}

%install
%cmake_install

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p %{name}.1 %{buildroot}%{_mandir}/man1

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest

%files
%license LICENSE
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.*

%files          devel
%{_includedir}/drat*.h
%{_libdir}/lib%{name}.so

%files          tools
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20190307.521caf1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20190307.521caf1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 0-0.12.20190307.521caf1
- Stop building for 32-bit x86

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20190307.521caf1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20190307.521caf1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 0-0.10.20190307.521caf1
- Add SPDX License tag for the tools subpackage

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20190307.521caf1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20190307.521caf1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 12 2021 Ryan Curtin <ryan@ratml.org> - 0-0.8.20190307.521caf1
- Updated for newer CLI11-2.0.0 dependency.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20190307.521caf1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20190307.521caf1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20190307.521caf1
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20190307.521caf1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20190307.521caf1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20190307.521caf1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun  6 2019 Jerry James <loganjerry@gmail.com> - 0-0.1.20190307.521caf1
- Initial RPM
