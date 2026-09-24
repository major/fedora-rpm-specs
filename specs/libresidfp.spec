Name:           libresidfp
Version:        1.2.2
Release:        1%{?dist}
Summary:        Cycle exact SID emulation
License:        GPL-2.0-or-later
URL:            https://github.com/libsidplayfp/%{name}
Source0:        https://github.com/libsidplayfp/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
This project is meant to replicate the SID as faithfully as possible while
keeping good performance for realtime use. It is not intended to expose
the chip internal state or adding fancy effects. Both the 6581 and the 8580
models are emulated.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
These are the files needed for compiling programs that use %{name}.


%package devel-doc
Summary:        API documentation for %{name}
BuildArch:      noarch

%description devel-doc
This package contains API documentation for %{name}.


%prep
%autosetup
# Regenerate autofoo stuff, it is better to always build this from source
rm -r aclocal.m4 build-aux
autoreconf -ivf


%build
%configure --disable-static
%make_build all doc


%install
%make_install


%check
%make_build check


%files
%doc AUTHORS NEWS.md README.md
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/residfp/
%{_libdir}/pkgconfig/%{name}.pc

%files devel-doc
%license COPYING
%doc docs/html


%changelog
* Wed Sep 23 2026 Karel Volný <kvolny@redhat.com> - 1.2.2-1
- initial Fedora package
