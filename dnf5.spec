%global project_version_major 5
%global project_version_minor 0
%global project_version_patch 14

Name:           dnf5
Version:        %{project_version_major}.%{project_version_minor}.%{project_version_patch}
Release:        2%{?dist}
Summary:        Command-line package manager
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/dnf5
Source0:        %{url}/archive/%{version}/dnf5-%{version}.tar.gz
Patch0001:      0001-Disable-tutorial-unit-tests.patch
Patch0002:      0002-fmt10-build-fix.patch
Patch0003:      0003-fmt10-time_point-fix.patch

Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
%if 0%{?fedora} <= 38
Requires:       dnf-data
%endif
Recommends:     bash-completion

# Remove if condition when Fedora 37 is EOL
%if 0%{?fedora} > 37
Provides:       microdnf = %{version}-%{release}
Obsoletes:      microdnf < 4
%endif

%if 0%{?fedora} > 38
Provides:       dnf = %{version}-%{release}
Obsoletes:      dnf < 5

Provides:       yum = %{version}-%{release}
Obsoletes:      yum < 5
%endif

# ========== build options ==========

%bcond_without dnf5daemon_client
%bcond_without dnf5daemon_server
%bcond_without libdnf_cli
%bcond_without dnf5
%bcond_without dnf5_plugins
%bcond_without plugin_actions
%bcond_without python_plugins_loader

%bcond_without comps
%bcond_without modulemd
%bcond_without zchunk

%bcond_with    html
%if 0%{?rhel} == 8
%bcond_with    man
%else
%bcond_without man
%endif

# TODO Go bindings fail to build, disable for now
%bcond_with    go
%bcond_without perl5
%bcond_without python3
%bcond_without ruby

%bcond_with    clang
%bcond_with    sanitizers
%bcond_without tests
%bcond_with    performance_tests
%bcond_with    dnf5daemon_tests

%if %{with clang}
    %global toolchain clang
%endif

# ========== versions of dependencies ==========

%global libmodulemd_version 2.5.0
%global librepo_version 1.15.0
%global libsolv_version 0.7.21
%global sqlite_version 3.35.0
%global swig_version 4
%global zchunk_version 0.9.11


# ========== build requires ==========

BuildRequires:  bash-completion
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gettext
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(librepo) >= %{librepo_version}
BuildRequires:  pkgconfig(libsolv) >= %{libsolv_version}
BuildRequires:  pkgconfig(libsolvext) >= %{libsolv_version}
BuildRequires:  pkgconfig(rpm) >= 4.17.0
BuildRequires:  pkgconfig(sqlite3) >= %{sqlite_version}
BuildRequires:  toml11-static

%if %{with clang}
BuildRequires:  clang
%else
BuildRequires:  gcc-c++
%endif

%if %{with tests}
BuildRequires:  createrepo_c
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  rpm-build
%endif

%if %{with comps}
BuildRequires:  pkgconfig(libcomps)
%endif

%if %{with modulemd}
BuildRequires:  pkgconfig(modulemd-2.0) >= %{libmodulemd_version}
%endif

%if %{with zchunk}
BuildRequires:  pkgconfig(zck) >= %{zchunk_version}
%endif

%if %{with html} || %{with man}
BuildRequires:  python3dist(breathe)
BuildRequires:  python3dist(sphinx) >= 4.1.2
BuildRequires:  python3dist(sphinx-rtd-theme)
%endif

%if %{with sanitizers}
# compiler-rt is required by sanitizers in clang
BuildRequires:  compiler-rt
BuildRequires:  libasan
BuildRequires:  liblsan
BuildRequires:  libubsan
%endif

%if %{with libdnf_cli}
# required for libdnf5-cli
BuildRequires:  pkgconfig(smartcols)
%endif

%if %{with dnf5daemon_server}
# required for dnf5daemon-server
BuildRequires:  pkgconfig(sdbus-c++) >= 0.8.1
BuildRequires:  systemd-rpm-macros
%if %{with dnf5daemon_tests}
BuildRequires:  dbus-daemon
BuildRequires:  polkit
BuildRequires:  python3-devel
BuildRequires:  python3dist(dbus-python)
%endif
%endif

# ========== language bindings section ==========

%if %{with perl5} || %{with ruby} || %{with python3}
BuildRequires:  swig >= %{swig_version}
%endif

%if %{with perl5}
# required for perl-libdnf5 and perl-libdnf5-cli
BuildRequires:  perl-devel
BuildRequires:  perl-generators
%if %{with tests}
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(warnings)
%endif
%endif

%if %{with ruby}
# required for ruby-libdnf5 and ruby-libdnf5-cli
BuildRequires:  pkgconfig(ruby)
%if %{with tests}
BuildRequires:  rubygem-test-unit
%endif
%endif

%if %{with python3}
# required for python3-libdnf5 and python3-libdnf5-cli
BuildRequires:  python3-devel
%endif

%description
DNF5 is a command-line package manager that automates the process of installing,
upgrading, configuring, and removing computer programs in a consistent manner.
It supports RPM packages, modulemd modules, and comps groups & environments.

%files
%{_bindir}/dnf5
%if 0%{?fedora} > 38
%{_bindir}/dnf
%{_bindir}/yum
%endif

# Remove if condition when Fedora 37 is EOL
%if 0%{?fedora} > 37
%{_bindir}/microdnf
%endif

%dir %{_sysconfdir}/dnf/dnf5-aliases.d
%doc %{_sysconfdir}/dnf/dnf5-aliases.d/README
%dir %{_datadir}/dnf5
%dir %{_datadir}/dnf5/aliases.d
%config %{_datadir}/dnf5/aliases.d/compatibility.conf
%dir %{_libdir}/dnf5
%dir %{_libdir}/dnf5/plugins
%doc %{_libdir}/dnf5/plugins/README
%dir %{_libdir}/libdnf5/plugins
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/dnf5
%dir %{_prefix}/lib/sysimage/dnf
%verify(not md5 size mtime) %ghost %{_prefix}/lib/sysimage/dnf/*
%license COPYING.md
%license gpl-2.0.txt
%{_mandir}/man8/dnf5.8.*
%{_mandir}/man8/dnf5-advisory.8.*
%{_mandir}/man8/dnf5-autoremove.8.*
%{_mandir}/man8/dnf5-clean.8.*
%{_mandir}/man8/dnf5-distro-sync.8.*
%{_mandir}/man8/dnf5-downgrade.8.*
%{_mandir}/man8/dnf5-download.8.*
%{_mandir}/man8/dnf5-environment.8.*
%{_mandir}/man8/dnf5-group.8.*
# TODO(jkolarik): history is not ready yet
# %%{_mandir}/man8/dnf5-history.8.*
%{_mandir}/man8/dnf5-install.8.*
%{_mandir}/man8/dnf5-leaves.8.*
%{_mandir}/man8/dnf5-makecache.8.*
%{_mandir}/man8/dnf5-mark.8.*
# TODO(jkolarik): module is not ready yet
# %%{_mandir}/man8/dnf5-module.8.*
%{_mandir}/man8/dnf5-reinstall.8.*
%{_mandir}/man8/dnf5-remove.8.*
%{_mandir}/man8/dnf5-repo.8.*
%{_mandir}/man8/dnf5-repoquery.8.*
%{_mandir}/man8/dnf5-search.8.*
%{_mandir}/man8/dnf5-swap.8.*
%{_mandir}/man8/dnf5-upgrade.8.*
%{_mandir}/man7/dnf5-comps.7.*
# TODO(jkolarik): filtering is not ready yet
# %%{_mandir}/man7/dnf5-filtering.7.*
%{_mandir}/man7/dnf5-installroot.7.*
# TODO(jkolarik): modularity is not ready yet
# %%{_mandir}/man7/dnf5-modularity.7.*
%{_mandir}/man7/dnf5-specs.7.*

# ========== libdnf5 ==========
%package -n libdnf5
Summary:        Package management library
License:        LGPL-2.1-or-later
#Requires:       libmodulemd{?_isa} >= {libmodulemd_version}
Requires:       libsolv%{?_isa} >= %{libsolv_version}
Requires:       librepo%{?_isa} >= %{librepo_version}
Requires:       sqlite-libs%{?_isa} >= %{sqlite_version}
%if 0%{?fedora} > 38
Conflicts:      dnf-data < 4.16.0
%endif

%description -n libdnf5
Package management library.

%files -n libdnf5
%if 0%{?fedora} > 38
%config(noreplace) %{_sysconfdir}/dnf/dnf.conf
%dir %{_sysconfdir}/dnf/vars
%dir %{_sysconfdir}/dnf/protected.d
%else
%exclude %{_sysconfdir}/dnf/dnf.conf
%endif
%dir %{_libdir}/libdnf5
%{_libdir}/libdnf5.so.1*
%license lgpl-2.1.txt
%{_var}/cache/libdnf/

# ========== libdnf5-cli ==========

%if %{with libdnf_cli}
%package -n libdnf5-cli
Summary:        Library for working with a terminal in a command-line package manager
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}

%description -n libdnf5-cli
Library for working with a terminal in a command-line package manager.

%files -n libdnf5-cli
%{_libdir}/libdnf-cli.so.1*
%license COPYING.md
%license lgpl-2.1.txt
%endif

# ========== dnf5-devel ==========

%package -n dnf5-devel
Summary:        Development files for dnf5
License:        LGPL-2.1-or-later
Requires:       dnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-devel%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli-devel%{?_isa} = %{version}-%{release}

%description -n dnf5-devel
Develpment files for dnf5.

%files -n dnf5-devel
%{_includedir}/dnf5/
%license COPYING.md
%license lgpl-2.1.txt


# ========== libdnf5-devel ==========

%package -n libdnf5-devel
Summary:        Development files for libdnf
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libsolv-devel%{?_isa} >= %{libsolv_version}

%description -n libdnf5-devel
Development files for libdnf.

%files -n libdnf5-devel
%{_includedir}/libdnf/
%dir %{_libdir}/libdnf5
%{_libdir}/libdnf5.so
%{_libdir}/pkgconfig/libdnf5.pc
%license COPYING.md
%license lgpl-2.1.txt


# ========== libdnf5-cli-devel ==========

%package -n libdnf5-cli-devel
Summary:        Development files for libdnf5-cli
License:        LGPL-2.1-or-later
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}

%description -n libdnf5-cli-devel
Development files for libdnf5-cli.

%files -n libdnf5-cli-devel
%{_includedir}/libdnf-cli/
%{_libdir}/libdnf-cli.so
%{_libdir}/pkgconfig/libdnf-cli.pc
%license COPYING.md
%license lgpl-2.1.txt


# ========== perl-libdnf5 ==========

%if %{with perl5}
%package -n perl-libdnf5
Summary:        Perl 5 bindings for the libdnf library
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}


%description -n perl-libdnf5
Perl 5 bindings for the libdnf library.

%files -n perl-libdnf5
%{perl_vendorarch}/libdnf5
%{perl_vendorarch}/auto/libdnf5
%license COPYING.md
%license lgpl-2.1.txt
%endif


# ========== perl-libdnf5-cli ==========

%if %{with perl5} && %{with libdnf_cli}
%package -n perl-libdnf5-cli
Summary:        Perl 5 bindings for the libdnf5-cli library
License:        LGPL-2.1-or-later
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}


%description -n perl-libdnf5-cli
Perl 5 bindings for the libdnf5-cli library.

%files -n perl-libdnf5-cli
%{perl_vendorarch}/libdnf5_cli
%{perl_vendorarch}/auto/libdnf5_cli
%license COPYING.md
%license lgpl-2.1.txt
%endif


# ========== python3-libdnf5 ==========

%if %{with python3}
%package -n python3-libdnf5
%{?python_provide:%python_provide python3-libdnf}
Summary:        Python 3 bindings for the libdnf library
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}

%description -n python3-libdnf5
Python 3 bindings for the libdnf library.

%files -n python3-libdnf5
%{python3_sitearch}/libdnf5
%{python3_sitearch}/libdnf5-*.dist-info
%license COPYING.md
%license lgpl-2.1.txt
%endif


# ========== python3-libdnf5-cli ==========

%if %{with python3} && %{with libdnf_cli}
%package -n python3-libdnf5-cli
%{?python_provide:%python_provide python3-libdnf5-cli}
Summary:        Python 3 bindings for the libdnf5-cli library
License:        LGPL-2.1-or-later
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}

%description -n python3-libdnf5-cli
Python 3 bindings for the libdnf5-cli library.

%files -n python3-libdnf5-cli
%{python3_sitearch}/libdnf5_cli
%{python3_sitearch}/libdnf5_cli-*.dist-info
%license COPYING.md
%license lgpl-2.1.txt
%endif


# ========== ruby-libdnf5 ==========

%if %{with ruby}
%package -n ruby-libdnf5
Summary:        Ruby bindings for the libdnf library
License:        LGPL-2.1-or-later
Provides:       ruby(libdnf) = %{version}-%{release}
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       ruby(release)

%description -n ruby-libdnf5
Ruby bindings for the libdnf library.

%files -n ruby-libdnf5
%{ruby_vendorarchdir}/libdnf5
%license COPYING.md
%license lgpl-2.1.txt
%endif


# ========== ruby-libdnf5-cli ==========

%if %{with ruby} && %{with libdnf_cli}
%package -n ruby-libdnf5-cli
Summary:        Ruby bindings for the libdnf5-cli library
License:        LGPL-2.1-or-later
Provides:       ruby(libdnf_cli) = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
Requires:       ruby(release)

%description -n ruby-libdnf5-cli
Ruby bindings for the libdnf5-cli library.

%files -n ruby-libdnf5-cli
%{ruby_vendorarchdir}/libdnf5_cli
%license COPYING.md
%license lgpl-2.1.txt
%endif


# ========== libdnf5-plugin-actions ==========

%if %{with plugin_actions}
%package -n libdnf5-plugin-actions
Summary:        Libdnf plugin that allows to run actions (external executables) on hooks
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}

%description -n libdnf5-plugin-actions
Libdnf plugin that allows to run actions (external executables) on hooks.

%files -n libdnf5-plugin-actions
%{_libdir}/libdnf5/plugins/actions.*
%endif


# ========== python3-libdnf5-plugins-loader ==========

%if %{with python_plugins_loader}
%package -n python3-libdnf5-python-plugins-loader
Summary:        Libdnf plugin that allows loading Python plugins
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       python3-libdnf5%{?_isa} = %{version}-%{release}

%description -n python3-libdnf5-python-plugins-loader
Libdnf plugin that allows loading Python plugins.

%files -n python3-libdnf5-python-plugins-loader
%{_libdir}/libdnf5/plugins/python_plugins_loader.*
%dir %{python3_sitelib}/libdnf_plugins/
%doc %{python3_sitelib}/libdnf_plugins/README
%endif


# ========== dnf5daemon-client ==========

%if %{with dnf5daemon_client}
%package -n dnf5daemon-client
Summary:        Command-line interface for dnf5daemon-server
License:        GPL-2.0-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
Requires:       dnf5daemon-server

%description -n dnf5daemon-client
Command-line interface for dnf5daemon-server.

%files -n dnf5daemon-client
%{_bindir}/dnf5daemon-client
%license COPYING.md
%license gpl-2.0.txt
%{_mandir}/man8/dnf5daemon-client.8.*
%endif


# ========== dnf5daemon-server ==========

%if %{with dnf5daemon_server}
%package -n dnf5daemon-server
Summary:        Package management service with a DBus interface
License:        GPL-2.0-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
Requires:       dbus
Requires:       polkit
%if 0%{?fedora} <= 38
Requires:       dnf-data
%endif

%description -n dnf5daemon-server
Package management service with a DBus interface.

%post -n dnf5daemon-server
%systemd_post dnf5daemon-server.service

%preun -n dnf5daemon-server
%systemd_preun dnf5daemon-server.service

%postun -n dnf5daemon-server
%systemd_postun_with_restart dnf5daemon-server.service

%files -n dnf5daemon-server
%{_sbindir}/dnf5daemon-server
%{_unitdir}/dnf5daemon-server.service
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.rpm.dnf.v0.conf
%{_datadir}/dbus-1/system-services/org.rpm.dnf.v0.service
%{_datadir}/dbus-1/interfaces/org.rpm.dnf.v0.*.xml
%{_datadir}/polkit-1/actions/org.rpm.dnf.v0.policy
%license COPYING.md
%license gpl-2.0.txt
%{_mandir}/man8/dnf5daemon-server.8.*
%{_mandir}/man8/dnf5daemon-dbus-api.8.*
%endif


# ========== dnf5-plugins ==========

%if %{with dnf5_plugins}
%package -n dnf5-plugins
Summary:        Plugins for dnf5
License:        LGPL-2.1-or-later
Requires:       dnf5%{?_isa} = %{version}-%{release}

%description -n dnf5-plugins
Core DNF5 plugins that enhance dnf5 with builddep, changelog, copr, and repoclosure commands.

%files -n dnf5-plugins
%{_libdir}/dnf5/plugins/*.so
%{_mandir}/man8/dnf5-builddep.8.*
%{_mandir}/man8/dnf5-copr.8.*
%{_mandir}/man8/dnf5-repoclosure.8.*
%endif


# ========== unpack, build, check & install ==========

%prep
%autosetup -p1 -n dnf5-%{version}


%build
%cmake \
    -DPACKAGE_VERSION=%{version} \
    -DPERL_INSTALLDIRS=vendor \
    \
    -DWITH_DNF5DAEMON_CLIENT=%{?with_dnf5daemon_client:ON}%{!?with_dnf5daemon_client:OFF} \
    -DWITH_DNF5DAEMON_SERVER=%{?with_dnf5daemon_server:ON}%{!?with_dnf5daemon_server:OFF} \
    -DWITH_LIBDNF5_CLI=%{?with_libdnf_cli:ON}%{!?with_libdnf_cli:OFF} \
    -DWITH_DNF5=%{?with_dnf5:ON}%{!?with_dnf5:OFF} \
    -DWITH_PLUGIN_ACTIONS=%{?with_plugin_actions:ON}%{!?with_plugin_actions:OFF} \
    -DWITH_PYTHON_PLUGINS_LOADER=%{?with_python_plugins_loader:ON}%{!?with_python_plugins_loader:OFF} \
    \
    -DWITH_COMPS=%{?with_comps:ON}%{!?with_comps:OFF} \
    -DWITH_MODULEMD=%{?with_modulemd:ON}%{!?with_modulemd:OFF} \
    -DWITH_ZCHUNK=%{?with_zchunk:ON}%{!?with_zchunk:OFF} \
    \
    -DWITH_HTML=%{?with_html:ON}%{!?with_html:OFF} \
    -DWITH_MAN=%{?with_man:ON}%{!?with_man:OFF} \
    \
    -DWITH_GO=%{?with_go:ON}%{!?with_go:OFF} \
    -DWITH_PERL5=%{?with_perl5:ON}%{!?with_perl5:OFF} \
    -DWITH_PYTHON3=%{?with_python3:ON}%{!?with_python3:OFF} \
    -DWITH_RUBY=%{?with_ruby:ON}%{!?with_ruby:OFF} \
    \
    -DWITH_SANITIZERS=%{?with_sanitizers:ON}%{!?with_sanitizers:OFF} \
    -DWITH_TESTS=%{?with_tests:ON}%{!?with_tests:OFF} \
    -DWITH_PERFORMANCE_TESTS=%{?with_performance_tests:ON}%{!?with_performance_tests:OFF} \
    -DWITH_DNF5DAEMON_TESTS=%{?with_dnf5daemon_tests:ON}%{!?with_dnf5daemon_tests:OFF} \
    \
    -DPROJECT_VERSION_MAJOR=%{project_version_major} \
    -DPROJECT_VERSION_MINOR=%{project_version_minor} \
    -DPROJECT_VERSION_PATCH=%{project_version_patch}
%cmake_build
%if %{with man}
    %cmake_build --target doc-man
%endif


%check
%if %{with tests}
    %ctest
%endif


%install
%cmake_install

%if 0%{?fedora} > 38
ln -sr %{buildroot}%{_bindir}/dnf5 %{buildroot}%{_bindir}/dnf
ln -sr %{buildroot}%{_bindir}/dnf5 %{buildroot}%{_bindir}/yum
%endif

# own dirs and files that dnf5 creates on runtime
mkdir -p %{buildroot}%{_prefix}/lib/sysimage/dnf
for files in \
    groups.toml modules.toml nevras.toml packages.toml \
    system.toml transaction_history.sqlite \
    transaction_history.sqlite-shm \
    transaction_history.sqlite-wal userinstalled.toml
do
    touch %{buildroot}%{_prefix}/lib/sysimage/dnf/$files
done

#find_lang {name}

# Remove if condition when Fedora 37 is EOL
%if 0%{?fedora} > 37
ln -sr %{buildroot}%{_bindir}/dnf5 %{buildroot}%{_bindir}/microdnf
%endif

%ldconfig_scriptlets


%changelog
* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 5.0.14-2
- Rebuilt due to fmt 10 update.
- Added upstream patches with fmt 10 build fixes.

* Wed Jun 14 2023 Packit <hello@packit.dev> - 5.0.14-1
- Modify libdnf5-devel to generate pkgconf(libdnf5)
- Handle unnamed environments in transaction table
- Return error exit code on RPM transaction failure
- Add `repoquery --file` option
- Add `repoquery --arch` option
- Add `repoquery --installonly` option
- Add `repoquery --extras`, `--upgrades` and `--recent` options
- Add `repoquery --changelogs` formatting option
- Don't complete ls alias
- Add rq command alias for `repoquery`
- Exclude dnf.conf when not installed
- Improve the download methods API
  - Switch to parameterless download methods and introduce setters for fail_fast and resume
  - Affected classes: libdnf::repo::FileDownloader, libdnf::repo::PackageDownloader

* Tue May 30 2023 Packit <nsella@redhat.com> - 5.0.13-2
- Update specfile to exclude dnf.conf for fedora < 39

* Mon May 29 2023 Packit <hello@packit.dev> - 5.0.13-1
- Release 5.0.13
- Fix resolve behavior for `download`
- Add a message when `--downloadonly` is used
- Add `--downloadonly` option to multiple commands

* Thu May 25 2023 Nicola Sella <nsella@redhat.com> - 5.0.12-1
- Release 5.0.12
- Have DNF update to DNF5
- Add dnf, yum obsoletes and provides
- Symlinks for `dnf` and `yum` binaries
- Move ownership of /etc/dnf/dnf.conf, /etc/dnf/vars, and /etc/dnf/protected.d from dnf-data to libdnf5
- Conflict with older versions of dnf-data that own these files/directories
- Print environments in the transaction table
- Add support for environmantal groups in dnf5daemon
- Handle unnamed groups in transaction table
- Update documentation for `distro-sync --skip-unavailable`
- Update documentation for `downgrade --skip-unavailable`
- Update documentation for `upgrade --skip-unavailable`
- Add repoquery `--files` and `files` querytag instead of `--list`
- Add getters to package for: debug, source, repo-name
- Add `repoquery --querytags` option
- Document `repoquery --queryformat`
- Add `repoquery --qf` alias to `repoquery --queryformat`
- Add get_depends() to package and --depends to repoquery
- Implement keepcache functionality (RhBug:2176384)
- API changes:
- libdnf::repo::PackageDownloader default ctor dropped (now accepting the Base object)
- libdnf::base::Transaction not accepting dest_dir anymore (implicitly taken from configuration)
- A note for existing users:
- Regardless of the keepcache option, all downloaded packages have been cached up until now.
- Starting from now, downloaded packages will be kept only until the next successful transaction (keepcache=False by default).
- To remove all existing packages from the cache, use the `dnf5 clean packages` command.
- goal: Split group specs resolution to separate method
- comps: Possibility to create an empty EnvironmentQuery
- `remove` command accepts `remove spec`
- Refactor remove positional arguments
- Remove duplicates from `group list` output
- Document `copr` plugin command
- Document `builddep` plugin command

* Fri May 19 2023 Petr Pisar <ppisar@redhat.com> - 5.0.11-3
- Rebuild against rpm-4.19 (https://fedoraproject.org/wiki/Changes/RPM-4.19)

* Fri May 19 2023 Nicola Sella <nsella@redhat.com> - 5.0.11-2
- Fix builds for arch non x86_64

* Thu May 18 2023 Packit <hello@packit.dev> - 5.0.11-1
- Release 5.0.11
- Add --contains-pkgs option to group info
- Add filter for containing package names
- Fix parameter names in documentation
- Document create parameter of RelDep::get_id method
- Document RepoQuery::filter_local
- Document repoclosure in man pages
- Document repoclosure command
- Implement repoclosure plugin
- package_query: filter_provides accepts also Reldep
- Fix download callbacks and many segfaults in dnf5daemon
- Add allow-downgrade configuration option
- Release 5.0.10
- dnf5-plugins: implement 'dnf5 copr'
- Add new configuration option exclude_from_weak_autodetect
- Add new config option exclude_from_weak
- Add repoquery --unneeded
- Fix handling of incorrect argument (RhBug:2192854)
- Add detect_release to public API
- Add group --no-packages option
- Add group upgrade command
- Enable group upgrades in transaction table
- Add --destdir option to download command
- Filter latest per argument for download command
- Add builddep --allowerasing
- download command: filter by priority, latest
- Remove --unneeded option from remove command
- Document autoremove differences from dnf4
- Add autoremove command
- state: Add package_types attribute to GroupState
- comps: Add conversion of PackageType to string(s)
- Add check-update alias for check-upgrade
- Add `check-upgrade --changelogs`

* Tue May 02 2023 Richard W.M. Jones <rjones@redhat.com> - 5.0.9-3
- Default tests off (temporarily, hopefully) on riscv64 arch.

* Wed Apr 26 2023 Nicola Sella <nsella@redhat.com> - 5.0.9-2
- Release 5.0.9 (Nicola Sella)
- Add `--userinstalled` to `repoquery` man page
- Implement `repoquery -userinstalled`
- Fix: progressbar: Prevent length_error exception (RhBug:2184271)
- Add dnf5-plugins directory in documentation
- Document `repoquery --leaves`
- Implement `repoquery --leaves`
- Implement new filters rpm::filter_leaves and rpm::filter_leaves_groups

* Thu Apr 13 2023 Nicola Sella <nsella@redhat.com> - 5.0.8-1
- Update to 5.0.8
- Improve error message in download command
- Add repoquery --latest-limit option
- Add dg, in, rei, rm aliases
- Add "up" and "update" aliases for "upgrade" command
- Update documentation with info about package spec expressions (RhBug:2160420)
- Add formatting options repoquery --requires, --provides..
- Remove unused repoquery nevra option
- Add `--queryformat` option to repoquery
- Improved progress bars
- Fix logic of installroot with deduplication
- Correctly load repos from installroot config file
- Improved loading and downloading of key files
- Improved modules: Change State to set and get the whole ModuleState
- New API method rpm::Package::is_available_locally
- Move description of DNF5 changes to doc
- Improved dnf5daemon logic and removed unused code
- Improved progress bar
- Improved handling of obsolete package installation
- Remove showdupesfromrepos config option
- man: Add info about download command destination
- Print resolve logs to stderr
- Fix double loading of system repo in dnf5daemon
- Set a minimal sqlite version
- Change to --use-host-config, warning suggesting --use-host-config
- Add capability to find binaries to resolve_spec
- Add pre-commit file
- Improved by fixing memory leaks
- Improved tests by enabling with multithreading
- Improve documentation  for list command
- Add compatibility alias ls->list
- Implement info command
- Implement list command
- Fix --exactdeps argument description

* Wed Mar 8 2023 Nicola Sella <nsella@redhat.com> - 5.0.7-1
- Document set/get vars in python api
- Document --strict deprecation
- New configuration option "disable_multithreading"
- Improved dnf5daemon to handle support groups and modules in return value
- Ignore inaccessible config unless path specified as --config=...
- Includes reordering and tweaks in advisories
- Add support for package changelogs in swig and tests
- Add many unit tests for dnf5 and python api
- Add new --skip-unavailable command line option
- Add search command
- Add new error for incorrect API usages
- Add a new method whether base was correctly initialized
- Improved python exceptions on undefined var
- transaction: Change API to run transaction without args
- Add explicit package version for libdnf5-cli
- Improved performance of packagequery

* Tue Feb 14 2023 Nicola Sella <nsella@redhat.com> - 5.0.6-1
- Add obsoletes of microdnf
- Many improvements related to internal logic and bugfixes
- Improvements in specfile
- Improved API, drop std::optional
- Use Autoapi instead of Autodoc to generate Python docs
- Improved documentation for modules

* Thu Jan 26 2023 Nicola Sella <nsella@redhat.com> - 5.0.5-1
- Fix build fail in rawhide
- Fixes in the concerning filesystem
- Fixes in the concerning modules
- Fixes in the concerning api

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Nicola Sella <nsella@redhat.com> - 5.0.4-2
- Backport downstream patch to disable unit tests for python tutorials
- Fix build in rawhide

* Thu Jan 12 2023 Nicola Sella <nsella@redhat.com> - 5.0.4-1
- Many fixes in perl bindings
- Test functions enhanced
- Extend unit tests for OptionString and OptionStringList

* Wed Jan 04 2023 Nicola Sella <nsella@redhat.com> - 5.0.3-1
- Add Python docs for: Base, Goal, RepoQuery, Package and PackageQuery
- Add docs for Python bindings: they are auto generated now
- Add --what* and --exactdeps options to repoquery
- Add "user enter password" to dnf5daemon functionalities
- Fix: remove repeating headers in transaction table
- Fix: Set status of download progress bar after successful download
- Fix: RepoDownloader::get_cache_handle: Don't set callbacks in LibrepoHandle
- Refactor internal utils
- Improved GlobalLogger
- Improved C++ API docs

* Thu Dec 08 2022 Nicola Sella <nsella@redhat.com> - 5.0.2-1
- Implement group remove command
- Improved options in config
- Add support for any number of user IDs in a PGP key
- Use new librepo PGP API
- remove gpgme dependency
- Improved exceptions and dnf5 errors
- Add dnf5-devel package
- Update README.md with up to date information
- Repoquery: Add --duplicates option
- Improved documentation for Repoquery, Upgrande and About section
- Add tutorials for python3 bindings
- dnf5-changes-doc: Add more structure using different headings
- Add ModuleQuery
- Improvements in comps logic

* Fri Nov 25 2022 Nicola Sella <nsella@rehat.com> - 5.0.1-1
- Update to 5.0.1
- Fix loading known keys for RepoGpgme
- Fix dnf5 progress_bar
- Improve modules: conflicting packages, weak resolve, active modules resolving
- plugins.hpp moved away from public headers and improvements logic
- Fix failing builds for i686 arch
- Add man pages to dnf5
- Fix non x86_64 builds
- Remove unimplemented commands

* Wed Nov 2 2022 Nicola Sella <nsella@redhat.com> - 5.0.0-2~pre
- Fix failing builds for i686 arch

* Mon Oct 31 2022 Nicola Sella <nsella@redhat.com> - 5.0.0-1~pre
- Add man pages to dnf5
- Fix non x86_64 builds
- Remove unimplemented commands

* Fri Sep 16 2022 Nicola Sella - <nsella@redhat.com> - 5.0.0-0~pre
- Dnf pre release build for Fedora
