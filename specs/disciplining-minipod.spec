%global libname liboscillator-disciplining
%global _description %{expand:
Library providing C disciplining algorithm used with oscillatord to discipling
oscillators using the minipod algorithm developed by Matthias Lorentz.}

Name:           disciplining-minipod
Version:        3.8.4
Release:        %autorelease
Summary:        Disciplining algorithm for Atomic Reference Time Card

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://github.com/Orolia2s/disciplining-minipod
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  sed

%description    %{_description}

%package -n     %{libname}
Summary:        %{summary}

%description -n %{libname} %{_description}

%package -n     %{libname}-devel
Summary:        Development files for %{libname}
Requires:       %{libname} = %{version}-%{release}

%description -n %{libname}-devel
This package contains development headers and files for %{libname}.

%prep
%autosetup -p1
# Drop forced optimization flag
sed -i 's/-O3//' CMakeLists.txt
# Do not install static library
sed -i 's/^install.*-static.*$//' src/CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%set_build_flags
%if 0%{?el8}
export CC="%{__cc}"
%endif
# build tests
%cmake -DBUILD_TESTS=true -DCMAKE_PREFIX_PATH="%{buildroot}%{_prefix}"
%cmake_build
# run tests
for t in test-checks test-utils test-minipod-lib test-fine-circular-buffer; do
# work around newer cmake and %{_vpath_builddir} difference
%if 0%{?el8}
  LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./test/$t
%else
  LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./%{_vpath_builddir}/test/$t
%endif
done

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/%{libname}.so.3*

%files -n %{libname}-devel
%{_includedir}/oscillator-disciplining
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc

%changelog
%autochangelog
