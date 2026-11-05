Name:           poly2tri
%global         commit a922022da4c0d3a55b1d6b6d634219caea653053
%global         shortcommit %{sub %{commit} 0 10}
%global         commitdate 20240130
%global         snapshot %{commitdate}.%{shortcommit}
Version:        0.0^%{snapshot}
Release:        %autorelease
Summary:        A 2D constrained Delaunay triangulation library
License:        BSD-3-Clause
URL:            https://github.com/greenm01/poly2tri
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
# The Makefile was created for purposes of this package
# Upstream provides WAF, but it builds example apps and not the library
Source1:        %{name}-Makefile
Source2:        %{name}-smoke.cc
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGL-devel

%description
Library based on the paper "Sweep-line algorithm for constrained Delaunay
triangulation" by V. Domiter and and B. Zalik.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -qn %{name}-%{commit}
cp %{SOURCE1} %{name}/Makefile
cp %{SOURCE2} %{name}/smoke.cc

iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && \
touch -r AUTHORS AUTHORS.conv && \
mv AUTHORS.conv AUTHORS

%build
cd %{name}
CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" %make_build
cd -

%install
install -Dpm0755 %{name}/lib%{name}.so.1.0 %{buildroot}%{_libdir}/lib%{name}.so.1.0
ln -s lib%{name}.so.1.0 %{buildroot}%{_libdir}/lib%{name}.so.1
ln -s lib%{name}.so.1.0 %{buildroot}%{_libdir}/lib%{name}.so

for H in %{name}/*/*.h %{name}/*.h; do
  install -Dpm0644 $H %{buildroot}%{_includedir}/$H
done

%check
cd %{name}
make check \
  CFLAGS="%{optflags}" \
  LDFLAGS="%{build_ldflags}" \
  SMOKE_INCLUDE="-I%{buildroot}%{_includedir}" \
  SMOKE_LIBDIR="%{buildroot}%{_libdir}"

%files
%doc AUTHORS LICENSE README 
%{_libdir}/lib%{name}.so.*

%files devel
%doc AUTHORS LICENSE README 
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}

%changelog
%autochangelog
