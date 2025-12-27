Name:           poly2tri
%global         rev 26242d0aa7b8
%global         date 20130501
%global         snapshot %{date}hg%{rev}
Version:        0.0^%{snapshot}
Release:        %autorelease
Summary:        A 2D constrained Delaunay triangulation library
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/greenm01/poly2tri
# hg clone %%{url}
# rm -rf %%{name}/.hg
# tar -pczf %%{name}-%%{rev}.tar.gz %%{name}
Source0:        %{name}-%{rev}.tar.gz
# The Makefile was created for purposes of this package
# Upstream provides WAF, but it builds example apps and not the library
Source1:        %{name}-Makefile
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
%setup -qn %{name}
cp %{SOURCE1} %{name}/Makefile

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

%files
%doc AUTHORS LICENSE README 
%{_libdir}/lib%{name}.so.*

%files devel
%doc AUTHORS LICENSE README 
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}

%changelog
%autochangelog
