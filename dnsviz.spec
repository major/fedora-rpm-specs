Name:           dnsviz
Version:        0.9.4
Release:        3%{?dist}
Summary:        Tools for analyzing and visualizing DNS and DNSSEC behavior

License:        GPLv2+
URL:            https://github.com/dnsviz/dnsviz
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  graphviz
BuildRequires:  make
BuildRequires:  python3-pygraphviz >= 1.3
BuildRequires:  python3-m2crypto >= 0.28.0
BuildRequires:  python3-dns >= 1.13
Requires:       python3-pygraphviz >= 1.3
Requires:       python3-m2crypto >= 0.28.0
Requires:       python3-dns >= 1.13

%description
DNSViz is a tool suite for analysis and visualization of Domain Name System
(DNS) behavior, including its security extensions (DNSSEC).  This tool suite
powers the Web-based analysis available at http://dnsviz.net/

%prep
%autosetup -p1

%build
%py3_build

%install
#XXX Normally the py3_install macro would be used here,
# but dnsviz/config.py is build with the install command,
# so install MUST call the build subcommand, so config.py
# will be proplerly placed.  With py3_install, the
# --skip-build argument is used.
%{__python3} %{py_setup} %{?py_setup_args} install -O1 --root %{buildroot} %{?*}

%check
pushd tests
mkdir bin
ln -s %{buildroot}%{_bindir}/%{name} bin/%{name}
export PYTHONPATH="%{buildroot}%{python3_sitelib}"
%{__python3} dnsviz_graph_options.py
# Cannot cope with not yet working DNSVIZ_SHARE_PATH
#%{__python3} dnsviz_graph_run.py
%{__python3} dnsviz_grok_options.py
%{__python3} dnsviz_grok_run.py
%{__python3} dnsviz_print_options.py
%{__python3} dnsviz_print_run.py
# Fails with dnsviz.resolver.ResolvConfError: No servers found in /etc/resolv.conf
#%{__python3} dnsviz_probe_options.py
#%{__python3} dnsviz_probe_run_offline.py
# No online tests in mock
#%{__python3} dnsviz_probe_run_online.py
popd

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-*.egg-info
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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Petr Menšík <pemensik@redhat.com> - 0.9.4-1
- Update to 0.9.4

* Thu Mar  11 2021 Casey Deccio
  0.9.3 release
* Fri Feb  5 2021 Casey Deccio
  0.9.2 release
* Tue Jan  19 2021 Casey Deccio
  0.9.1 release
* Fri Jan  8 2021 Casey Deccio
  0.9.0 release
* Wed Feb  6 2019 Casey Deccio
  0.8.1 release
* Fri Jan  25 2019 Casey Deccio
  0.8.0 release
