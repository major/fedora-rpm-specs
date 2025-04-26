%bcond_without tests
%bcond_with    all_tests

Name:           dnsviz
Version:        0.11.1
Release:        %autorelease
Summary:        Tools for analyzing and visualizing DNS and DNSSEC behavior

License:        GPL-2.0-or-later
URL:            https://github.com/dnsviz/dnsviz
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

Patch1:         dnsviz-0.11-no-sha1.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  graphviz
BuildRequires:  make

BuildRequires:  python3-pygraphviz >= 1.3
BuildRequires:  python3-cryptography
BuildRequires:  python3-dns >= 1.13
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  bind
BuildRequires:  bind-dnssec-utils
Requires:       python3-pygraphviz >= 1.3
Requires:       python3-dns >= 1.13

%description
DNSViz is a tool suite for analysis and visualization of Domain Name System
(DNS) behavior, including its security extensions (DNSSEC).  This tool suite
powers the Web-based analysis available at http://dnsviz.net/

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%check
%if %{with tests}
export DNSVIZ_SHARE_PATH="%{buildroot}%{_datadir}%{name}"
%if %{with all_tests}
  if ! [ -f /etc/resolv.conf ]; then
    # mock may not have any resolv.conf
    echo "nameserver 127.0.0.1" | tee /etc/resolv.conf
    OWN_RESOLV=y
  fi
  %pytest
  if [ "$OWN_RESOLV" = y ]; then
    rm -f /etc/resolv.conf
  fi
%else
  %pytest -k "not probe_options and not probe_run_online and not test_dnsviz_graph_output_format and not _online"
%endif
%endif

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_defaultdocdir}/%{name}/dnsviz-graph.html
%{_defaultdocdir}/%{name}/images/*png
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-probe.1*
%{_mandir}/man1/%{name}-graph.1*
%{_mandir}/man1/%{name}-grok.1*
%{_mandir}/man1/%{name}-print.1*
%{_mandir}/man1/%{name}-query.1*

%changelog
%autochangelog
