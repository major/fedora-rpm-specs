# The only release tarball is old, so we check out of git.
%global gitdate     20160901
%global commit      9ab9717cf7d1be1a85b165a8eacb71b9e5831113
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           mcqd
Version:        1.0.0
Release:        10.%{gitdate}.%{shortcommit}%{?dist}
Summary:        Maximum clique in an undirected graph

License:        GPL-3.0-or-later
URL:            http://insilab.org/maxclique/
Source0:        https://gitlab.com/janezkonc/mcqd/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# Sagemath patch to reduce verbosity
Patch0:         %{name}-silent.patch
# Split the main function out into its own file to facilitate building a library
Patch1:         %{name}-library.patch

BuildRequires:  gcc-c++

%description
This package computes MaxCliqueDyn, a fast exact algorithm for finding a
maximum clique in an undirected graph.

%package        devel
Summary:        Headers and library links for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and library links for building applications that use %{name}.

%package        tool
Summary:        Command line tool to compute maximum clique
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tool
This package provides a command line tool for computing the maximum
clique of an undirected graph.  Input is in DIMACS format.

%prep
%autosetup -p0 -n %{name}-%{commit}

# Change from Windows to Unix newlines
sed -i 's/\r//' *.{cpp,h}

%build
# Build the library
g++ -fPIC -shared %{build_cxxflags} %{build_ldflags} -Wl,-h,lib%{name}.so.0 \
    -o lib%{name}.so.0.0.0 %{name}.cpp
ln -s lib%{name}.so.0.0.0 lib%{name}.so.0
ln -s lib%{name}.so.0 lib%{name}.so

# Build the binary
g++ %{build_cxxflags} %{build_ldflags} -o %{name} %{name}-main.cpp -L. -lmcqd

%install
# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -p lib%{name}.so.0.0.0 %{buildroot}%{_libdir}
ln -s lib%{name}.so.0.0.0 %{buildroot}%{_libdir}/lib%{name}.so.0
ln -s lib%{name}.so.0 %{buildroot}%{_libdir}/lib%{name}.so

# Install the header file
mkdir -p %{buildroot}%{_includedir}
cp -p %{name}.h %{buildroot}%{_includedir}

# Install the binary
mkdir -p %{buildroot}%{_bindir}
cp -p %{name} %{buildroot}%{_bindir}

%check
LD_LIBRARY_PATH=$PWD ./mcqd test.clq > test.log 2>&1
[ $(grep -F 'Maximum clique:' test.log | wc -l) -eq 2 ]

%files
%license COPYING
%doc README.md
%{_libdir}/lib%{name}.so.0*

%files          devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%files          tool
%{_bindir}/%{name}

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10.20160901.9ab9717
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9.20160901.9ab9717
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 1.0.0-8.20160901.9ab9717
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8.20160901.9ab9717
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7.20160901.9ab9717
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6.20160901.9ab9717
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5.20160901.9ab9717
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4.20160901.9ab9717
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.20160901.9ab9717
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2.20160901.9ab9717
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul  8 2019 Jerry James <loganjerry@gmail.com> - 1.0.0-1.20160901.9ab9717
- Initial RPM
