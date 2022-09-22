Name:           derrick
Version:        0.3
Release:        19%{?dist}
Summary:        A Simple Network Stream Recorder

License:        BSD
URL:            https://github.com/rieck/derrick
Source0:        https://github.com/rieck/derrick/archive/s%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires:  libpcap-devel
BuildRequires:  libnet-devel
BuildRequires:  libnids-devel
BuildRequires:  uthash-devel
BuildRequires: make

%description
Derrick is a simple tool for recording data streams of TCP and UDP traffic.
It shares similarities with other network recorders, such as tcpflow and
wireshark, where it is more advanced than the first and clearly inferior to
the latter.

Derrick has been specifically designed to monitor application-layer
communication. In contrast to other tools the application data is logged in
a line-based ASCII format. Common UNIX tools, such as grep, sed & awk, can
be directly applied. Even replay of recorded communication is straight
forward using netcat.

Derrick supports on-the-fly compression and rotation of log files. The
payloads of TCP sessions are re-assembled using Libnids and can be merged
or truncated. UDP payloads are logged as-is. Details of lower network
layers are omitted.

%prep
%setup -q -n %{name}-s%{version}
##rm -rf %{name}-s%{version}/src/uthash.h

%build
./bootstrap
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

%check
make check

%files
%doc COPYING README.md
%{_mandir}/man1/%{name}.*
%{_bindir}/%{name}

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Björn Esser <besser82@fedoraproject.org> - 0.3-17
- Rebuild(uthash)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 13 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.3-3
- Remove embedded uthash

* Tue Apr 08 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.3-2
- Remove compiler flag and char from versioning

* Tue Aug 13 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.3-1
- Updated to release tarball

* Tue Jan 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0-1
- Initial spec
