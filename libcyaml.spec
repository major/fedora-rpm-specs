%global forgeurl https://github.com/tlsa/libcyaml
Version:        1.4.1
%forgemeta

Name:           libcyaml
Release:        %autorelease
Summary:        C library for reading and writing YAML
License:        ISC
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libyaml-devel

%description
LibCYAML is a C library for reading and writing structured YAML documents. It is
written in ISO C11 and licensed under the ISC licence.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%forgeautosetup -p1

%build
%make_build

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_lib}

rm %{buildroot}%{_libdir}/libcyaml.a

%check
make test

%files
%license
%doc README.md
%{_libdir}/libcyaml.so.1*

%files devel
%{_includedir}/cyaml/
%{_libdir}/libcyaml.so
%{_libdir}/pkgconfig/libcyaml.pc

%changelog
%autochangelog
