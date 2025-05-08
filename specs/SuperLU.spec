%global genname superlu

Name:		SuperLU
Version:	7.0.1
Release:	%autorelease
Summary:	Subroutines to solve sparse linear systems
License:	BSD-2-Clause AND GPL-2.0-or-later
URL:		https://portal.nersc.gov/project/sparse/superlu/
Source0:	https://github.com/xiaoyeli/superlu/archive/v%{version}/%{genname}-%{version}.tar.gz

# Use a pre-made configuration file for Make
Source1:     %{name}-fedora-make.inc.in

Patch0:	 %{genname}-removemc64.patch

# Fix ldflags of example files
Patch1:      %{name}-fix_example_builds.patch

# Fix 'VERSION_BugFix' number
Patch2:      %{name}-%{version}-fix_version.patch

BuildRequires: pkgconfig(flexiblas)
%if 0%{?epel}
BuildRequires:	epel-rpm-macros
%endif
BuildRequires:	metis-devel
BuildRequires:	make
BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-gfortran
BuildRequires:	csh

%description
SuperLU contains a set of subroutines to solve a sparse linear system 
A*X=B. It uses Gaussian elimination with partial pivoting (GEPP). 
The columns of A may be preordered before factorization; the 
preordering for sparsity is completely separate from the factorization.

%package devel
Summary:	Header files and libraries for SuperLU development
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel 
The %{name}-devel package contains the header files
and libraries for use with %{name} package.

%package doc
Summary:	Documentation and Examples for SuperLU
BuildArch:	noarch
%description doc
The %{name}-doc package contains all the help HTML documentation.

%prep
%autosetup -n %{genname}-%{version} -N

%patch -P 0 -p1 -b .backup
%patch -P 1 -p1 -b .backup
%patch -P 2 -p1 -b .backup

rm -f make.inc
cp -pf %{SOURCE1} make.inc.in

# Remove bundled BLAS
rm -rf CBLAS

rm -fr SRC/mc64ad.f.bak
find . -type f | sed -e "/TESTING/d" | xargs chmod a-x

# Remove the shippped executables from EXAMPLE
find EXAMPLE -type f | while read file
do
   [ "$(file $file | awk '{print $2}')" = ELF ] && rm $file || :
done

# Change optimization level
sed -e 's|-O0|-O2|g' -i SRC/CMakeLists.txt

%build
%cmake \
   -Denable_internal_blaslib:BOOL=NO \
   -DXSDK_ENABLE_Fortran:BOOL=OFF \
   -DCMAKE_Fortran_FLAGS_RELEASE:STRING="%{__global_fflags}" \
   -DTPL_BLAS_LIBRARIES="`pkg-config --libs flexiblas`" \
   -DTPL_ENABLE_METISLIB:BOOL=ON \
   -DTPL_METIS_INCLUDE_DIRS:PATH=%{_includedir} \
   -DTPL_METIS_LIBRARIES:FILEPATH=%{_libdir}/libmetis.so \
   -DCMAKE_BUILD_TYPE:STRING=Release \
   -DCMAKE_INSTALL_INCLUDEDIR:PATH=include/%{name} \
   -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
   -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES
%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:MATGEN
%ctest

%files
%license License.txt
%{_libdir}/libsuperlu.so.7
%{_libdir}/libsuperlu.so.%{version}

%files devel
%{_includedir}/%{name}/
%{_libdir}/libsuperlu.so
%{_libdir}/cmake/%{genname}/
%{_libdir}/pkgconfig/%{genname}.pc

%files doc
%license License.txt
%doc DOC

%changelog
%autochangelog
