%global forgeurl https://github.com/troglobit/%{name}

Name:           libuev
Version:        2.4.1

%forgemeta

Release:        %autorelease
Summary:        Simple event loop for Linux
License:        MIT
URL:     %{forgeurl}
Source0: %{forgesource}

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  make

%description
libuEv is a small event loop that wraps the Linux epoll() family
of APIs. It is similar to the more established libevent, libev 
and the venerable Xt(3) event loop. The µ in the name refers to 
both its limited feature set and the size impact of the library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for
developing application that use %{name}.

%prep
%setup -q
./autogen.sh

%build
%configure --disable-static
%make_build

%check
make check

%install
%make_install

# examples directory: remove unuseful files
find examples -type f \( -name "Makefile*" -or -name ".gitignore" \) -exec rm -f {} ';'

# remove docs from buildroot
rm -rf %{buildroot}%{_docdir}/libuev

# remove something unnecessary
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%license LICENSE
%doc README.md AUTHORS LICENSE ChangeLog.md
%{_libdir}/%{name}.so.3*

%files devel
%doc examples
%{_includedir}/uev
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
