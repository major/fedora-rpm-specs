Name:           jurand
Version:        1.3.0
Release:        1%{?dist}
Summary:        A tool for manipulating Java symbols
License:        Apache-2.0
URL:            https://github.com/fedora-java/jurand

Source0:        https://github.com/fedora-java/jurand/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++

BuildRequires:  asciidoc
BuildRequires:  diffutils
BuildRequires:  xmlto

%description
The tool can be used for patching .java sources in cases where using sed is
insufficient due to Java language syntax. The tool follows Java language rules
rather than applying simple regular expressions on the source code.

%prep
%setup -q

%build
./build.sh
./build_manpages.sh

%install
export buildroot=%{buildroot}
export bindir=%{_bindir}
export rpmmacrodir=%{_rpmmacrodir}
export mandir=%{_mandir}/man7

./install.sh

%check
./test.sh

%files -f target/installed_files
%dir %{_rpmconfigdir}
%dir %{_rpmmacrodir}
%license LICENSE NOTICE
%doc README.md

%changelog
* Wed Mar 15 2023 Marian Koncek <mkoncek@redhat.com> - 1.3.0-1
- Update to upstream version 1.3.0

* Wed Mar 08 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-2
- Skip interface keyword as annotation in name matching only

* Wed Mar 08 2023 Marian Koncek <mkoncek@redhat.com> - 1.2.0-1
- Update to upstream version 1.2.0

* Tue Mar 07 2023 Marian Koncek <mkoncek@redhat.com> - 1.1.0-1
- Update to upstream version 1.1.0

* Fri Mar 03 2023 Marian Koncek <mkoncek@redhat.com> - 1.0.2-1
- Update to upstream version 1.0.2

* Wed Mar 01 2023 Marian Koncek <mkoncek@redhat.com> - 1.0.0-1
- Initial build
