# there is no debug package
%global debug_package %{nil}

Name:           half
Version:        2.2.0
Release:        1%{?dist}
Summary:        A C++ half-precision floating point type
License:        MIT

URL:            http://sourceforge.net/projects/half
Source0:        %{url}/files/%{name}/%{version}/%{name}-%{version}.zip
BuildArch:      noarch

%description
This is a C++ header-only library to provide an IEEE-754 conformant
half-precision floating point type along with corresponding arithmetic
operators, type conversions and common mathematical functions. It aims
for both efficiency and ease of use, trying to accurately mimic the
behaviour of the builtin floating point types at the best performance
possible. It automatically uses and provides C++11 features when
possible, but stays completely C++98-compatible when neccessary.

%package devel
Summary:        A C++ half-precision floating point type
Provides:       %{name}-static = %{version}-%{release}

%description devel
This is a C++ header-only library to provide an IEEE-754 conformant
half-precision floating point type along with corresponding arithmetic
operators, type conversions and common mathematical functions. It aims
for both efficiency and ease of use, trying to accurately mimic the
behaviour of the builtin floating point types at the best performance
possible. It automatically uses and provides C++11 features when
possible, but stays completely C++98-compatible when neccessary.

%prep
rm -rf %{name}-%{version}
unzip -d %{name}-%{version} %{SOURCE0}
cd %{name}-%{version}
# change dos endings to unix
sed -i "s|\r||g" include/half.hpp
sed -i "s|\r||g" LICENSE.txt
sed -i "s|\r||g" README.txt

%install
cd %{name}-%{version}
mkdir -p %{buildroot}%{_includedir}
install -m 644 include/half.hpp %{buildroot}%{_includedir}

mkdir -p %{buildroot}%{_docdir}/%{name}/
install -m 644 LICENSE.txt %{buildroot}%{_docdir}/%{name}/
install -m 644 README.txt %{buildroot}%{_docdir}/%{name}/

%files devel
%doc %{_docdir}/%{name}/README.txt
%license %{_docdir}/%{name}/LICENSE.txt
%{_includedir}/half.hpp

%changelog
* Wed Aug 9 2023 Tom Rix <trix@redhat.com> - 2.2.0-1
- Initial package
