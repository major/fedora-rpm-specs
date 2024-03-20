# Force out of source build
%undefine __cmake_in_source_build
%global         soversion 1.13.0

Name:           partio
Version:        1.17.3
Release:        %autorelease
Summary:        Library for manipulating common animation particle

License:        BSD-3-Clause-Modification
URL:            https://github.com/wdas/%{name}
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
# Disabled due to failure to get name
#BuildRequires:  help2man
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  swig

%description
C++ (with python bindings) library for easily reading/writing/manipulating 
common animation particle formats such as PDB, BGEO, PTC.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
%{summary}

%package        libs
Summary:        Core %{name} libraries

%description    libs
C++ (with python bindings) library for easily reading/writing/manipulating 
common animation particle formats such as PDB, BGEO, PTC.

%package -n python3-%{name}
Summary:        %{summary}
BuildRequires:  pkgconfig(python3)

%description -n python3-%{name} 
The python3-%{name} contains Python 3 binning for the library.

%prep
%autosetup -p1

# Fix all Python shebangs recursively in .
%py3_shebang_fix .

%build
%cmake \
 -DCMAKE_PREFIX_PATH=%{_prefix} \
 -DCXXFLAGS_STD=c++17
%cmake_build

%install
%cmake_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

#Remove files from unversioned python directory
rm -f %{buildroot}%{_libdir}/python/site-packages/*.py

#Remove all tests containing arch-depedents binaries
rm -rf %{buildroot}%{_datadir}/%{name}/test

%files
%license LICENSE
%doc README.md
%{_bindir}/part{attr,convert,edit,info,inspect,json,view}
%{_datadir}/swig/%{name}.i      

%files devel
%{_includedir}/Partio{,Attribute,Iterator,Vec3}.h
%{_libdir}/lib%{name}.so

%files doc
%doc %{_defaultdocdir}/%{name}/html

%files libs
%license LICENSE
%{_libdir}/lib%{name}.so.{1,%{soversion}}

%files -n python3-%{name}
%{python3_sitearch}/_%{name}.so
%pycached %{python3_sitearch}/*.py

%changelog
%autochangelog
