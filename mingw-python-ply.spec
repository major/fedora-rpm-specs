%{?mingw_package_header}

%global pkgname ply

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       3.11
Release:       1%{?dist}
BuildArch:     noarch

License:       BSD
URL:           http://www.dabeaz.com/ply/
Source0:       http://www.dabeaz.com/ply/%{pkgname}-%{version}.tar.gz

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-setuptools


%description
MinGW Windows Python %{pkgname} library.


%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname} library

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 %{pkgname} library.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname} library

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python3 %{pkgname} library.


%prep
%autosetup -p1 -n %{pkgname}-%{version}

# extract license block from beginning of README.md
grep -B1000 "POSSIBILITY OF SUCH DAMAGE" README.md > LICENSE


%build
%{mingw32_py3_build}
%{mingw64_py3_build}


%install
%{mingw32_py3_install}
%{mingw64_py3_install}


%files -n mingw32-python3-%{pkgname}
%license LICENSE
%{mingw32_python3_sitearch}/%{pkgname}/
%{mingw32_python3_sitearch}/%{pkgname}-%{version}-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_python3_sitearch}/%{pkgname}/
%{mingw64_python3_sitearch}/%{pkgname}-%{version}-py%{mingw64_python3_version}.egg-info/


%changelog
* Thu Jul 28 2022 Sandro Mani <manisandro@gmail.com> - 3.11-1
- Update to 3.11
