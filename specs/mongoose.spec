%bcond_with check

Name:		mongoose
Version:	7.21

%global forgeurl https://github.com/cesanta/mongoose
# upstream use tag without the v prefix
%global tag %{version}

%global _soversion %(v=%{version}; IFS='.'; set -- ${v}; echo $1)

%forgemeta

Summary:	Embedded Web Server
Release:	%autorelease
License:	GPL-2.0-only
URL:		https://mongoose.ws/
Source:		%{forgesource}

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(openssl)


%description
Mongoose is a network library for C/C++. It implements event-driven
non-blocking APIs for TCP, UDP, HTTP, WebSocket, MQTT. It is designed
for connecting devices and bringing them online. On the market since
2004, used by vast number of open source and commercial products - it
even runs on the International Space Station! Mongoose makes embedded
network programming fast, robust, and easy.

%package devel
Summary:	Header files and development libraries for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}.

%package static
Summary:	Static library for %{name}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package contains static libraries for %{name}.

%prep
%forgeautosetup -p1

%build
cd test
%make_build linux-libs VERSION=%{_soversion} SSL=OPENSSL

%install
mkdir -p %{buildroot}%{_libdir} %{buildroot}%{_includedir}
cd test
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} INCLUDEDIR=%{_includedir} VERSION=%{_soversion} SSL=OPENSSL

pushd %{buildroot}%{_libdir}
mv lib%{name}.so.%{_soversion} lib%{name}.so.%{version}
# I have absolutely no idea how they've done that
chmod +x lib%{name}.so.%{version}
ln -s lib%{name}.so.%{version} lib%{name}.so.%{_soversion}
popd

# unit tests requires internet and depend on external site behaviors, disable for now
%if %{with check}
%check
cd test
%_set_build_flags
%make_build test
%endif

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.%{_soversion}*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%files static
%{_libdir}/lib%{name}.a

%changelog
%autochangelog
