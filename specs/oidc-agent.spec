%if %{?fedora}%{!?fedora:0} >= 38
%global maketrace --debug=print
%else
%global maketrace .SHELLFLAGS=-xc
%endif

Name:		oidc-agent
Version:	5.2.3
Release:	2%{?dist}
Summary:	Managing OpenID Connect tokens on the command line

License:	MIT AND ISC AND LGPL-2.1-or-later AND BSD-2-Clause
URL:		https://github.com/indigo-dc/%{name}
Source0:	%{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
#		clibs-list-devel not available for ix86....
ExcludeArch:	%{ix86}

BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	cjson-devel
BuildRequires:	clibs-list-devel
BuildRequires:	curl-devel
BuildRequires:	libsodium-devel
BuildRequires:	libmicrohttpd-devel
BuildRequires:	glib2-devel
BuildRequires:	qrencode-devel
BuildRequires:	gtk3-devel
%if %{?fedora}%{!?fedora:0}
%global webkitgtk webkit2gtk-4.1
BuildRequires:	webkit2gtk4.1-devel
%else
%global webkitgtk webkit2gtk-4.0
BuildRequires:	webkitgtk4-devel
#BuildRequires:	webkit2gtk3-devel (equivalent, but doesn't work on EPEL 7)
#BuildRequires:	webkit2gtk4.0-devel (equivalent, but doesn't work on EPEL)
%endif
BuildRequires:	systemd-rpm-macros
BuildRequires:	help2man

%description
oidc-agent is a set of tools to manage OpenID Connect tokens and make
them easily usable from the command line. We followed the ssh-agent
design, so users can handle OIDC tokens in a similar way as they do
with ssh keys.

oidc-agent is usually started in the beginning of an X-session or a
login session. Through use of environment variables the agent can be
located and used to handle OIDC tokens.

The agent initially does not have any account configurations
loaded. You can load an account configuration by using
oidc-add. Multiple account configurations may be loaded in oidc-agent
concurrently. oidc-add is also used to remove a loaded configuration
from oidc-agent. oidc-gen is used to initially generate an account
configurations file.

%package cli
Summary:	Command line tool for obtaining OpenID Connect tokens
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description cli
oidc-agent is a set of tools to manage OpenID Connect tokens and make
them easily usable from the command line. These tools follow ssh-agent
design, so OIDC tokens can be handled in a similar way as ssh keys.
The agent stores multiple configurations and their associated refresh
tokens securely.

This tool consists of five programs:
  - oidc-agent that handles communication with the OIDC provider
  - oidc-gen that generates config files
  - oidc-add that loads (and unloads) configuration into the agent
  - oidc-token that can be used to get access token on the command line
  - oidc-key-chain that re-uses oidc-agent across logins

%package desktop
Summary:	GUI integration for obtaining OpenID Connect tokens
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-cli = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < %{version}-%{release}

%description desktop
Desktop integration files for oidc-gen and oidc-agent.

This package adds two ways for supporting the usage of oidc-agent in a
graphical environment:
 - The .desktop file to leverage browser integration to support the
   authorization code flow in oidc-gen.
 - The Xsession file to consistently set the environment variables
   necessary to for client tools to connect to the oidc-agent daemon.

%package libs
Summary:	Library for oidc-agent

%description libs
oidc-agent is a command line tool for obtaining OpenID Connect tokens
on the command line.

This package provides a library for easy communication with oidc-agent.
Applications can use this library to request access tokens from
oidc-agent.

%package devel
Summary:	Headers for the oidc-agent library
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
oidc-agent is a command line tool for obtaining OpenID Connect tokens
on the command line.

This package provides headers for the oidc-agent library.

%prep
%setup -q

# Remove bundled cJSON and clib-list (use system versions)
rm -rf lib/cJSON lib/list

%build
%set_build_flags
%make_build %{maketrace} WEBKITGTK=%{webkitgtk}

%install
%set_build_flags
%make_install install_includes %{maketrace} \
	WEBKITGTK=%{webkitgtk} \
	PREFIX=%{buildroot} \
	INCLUDE_PATH=%{buildroot}%{_includedir} \
	LIB_PATH=%{buildroot}%{_libdir} \
	BIN_AFTER_INST_PATH=%{_prefix} \
	CONFIG_AFTER_INST_PATH=%{_sysconfdir}
ln -s liboidc-agent.so.%{version} %{buildroot}%{_libdir}/liboidc-agent.so

%post cli
%tmpfiles_create %{name}.conf

%files cli
%{_bindir}/oidc-add
%{_bindir}/oidc-agent
%{_bindir}/oidc-agent-service
%{_bindir}/oidc-gen
%{_bindir}/oidc-keychain
%{_bindir}/oidc-token
%{_bindir}/oidc-tokensh
%{bash_completions_dir}/oidc-add
%{bash_completions_dir}/oidc-agent
%{bash_completions_dir}/oidc-agent-service
%{bash_completions_dir}/oidc-gen
%{bash_completions_dir}/oidc-keychain
%{bash_completions_dir}/oidc-token
%{_mandir}/man1/oidc-add.1*
%{_mandir}/man1/oidc-agent.1*
%{_mandir}/man1/oidc-agent-service.1*
%{_mandir}/man1/oidc-gen.1*
%{_mandir}/man1/oidc-keychain.1*
%{_mandir}/man1/oidc-token.1*
%{_mandir}/man1/oidc-tokensh.1*
%{_tmpfilesdir}/%{name}.conf
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/issuer.config
%dir %{_sysconfdir}/%{name}/issuer.config.d
%config(noreplace) %{_sysconfdir}/%{name}/issuer.config.d/*
%config(noreplace) %{_sysconfdir}/%{name}/oidc-agent-service.options
%license LICENSE
%doc CHANGELOG.md PRIVACY README.md

%files desktop
%{_bindir}/oidc-prompt
%{_mandir}/man1/oidc-prompt.1*
%dir %{_sysconfdir}/X11/Xsession.d
%config(noreplace) %{_sysconfdir}/X11/Xsession.d/91oidc-agent
%{_datadir}/applications/oidc-gen.desktop

%files libs
%{_libdir}/liboidc-agent.so.5*
%license LICENSE

%files devel
%{_includedir}/%{name}
%{_libdir}/liboidc-agent.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.3-1
- Update to version 5.2.3

* Thu Sep 12 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.2-1
- Update to version 5.2.2

* Mon Sep 02 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.1-1
- Update to version 5.2.1

* Thu Aug 29 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.0-1
- Update to version 5.2.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.1.0-1
- Update to version 5.1.0

* Thu Oct 05 2023 Remi Collet <remi@remirepo.net> - 5.0.1-2
- rebuild for new libsodium

* Mon Sep 04 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.0.1-1
- Update to version 5.0.1
- Drop patch oidc-agent-webkit.patch (previously backported
- Drop patch oidc-agent.patch (accepted upstram)

* Sun Aug 20 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.5.2-2
- Use webkit2gtk-4.1 (Fedora)

* Mon Jul 10 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.5.2-1
- Initial build for Fedora and EPEL
