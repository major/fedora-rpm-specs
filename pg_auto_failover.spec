%bcond_without docs
%bcond_without llvmjit
%global precise_version %{?epoch:%epoch:}%version-%release

Name:           pg_auto_failover
Version:        2.0
Release:        2%{?dist}
Summary:        Postgres extension and service for automated failover and high-availability

License:        ASL 1.0
URL:            https://github.com/citusdata/%{name}/
Source0:        https://github.com/citusdata/%{name}/archive/refs/tags/v%{version}.tar.gz

# Requirements for pg_auto_failover code
# openssl-devel provides necessary cryptography library
# build process require the same libraries that were used when PostgreSQL was built
# pg_config --libs
BuildRequires:  gcc-c++ openssl-devel zlib-devel libxslt-devel readline-devel pam-devel
# PostgreSQL libraries and development headers (used by pg_auto_failover)
BuildRequires:  postgresql-static postgresql-server-devel
BuildRequires:  lz4-devel
# Requirements for doc and man files
BuildRequires:  python3-sphinx
%if %{with docs}
# Requirements for doc files
BuildRequires: python3-sphinx_rtd_theme graphviz
%endif

# Requirements for building latex documentation
BuildRequires: texlive-scheme-basic tex(luatex85.sty) tex(standalone.cls) tex(cfr-lm.sty) 
# Required tools for building latex documentation
BuildRequires: latexmk poppler-utils

# Fedora 35 include new dependency with postgresql-server-devel package:
# postgresql-private-devel. It conflicts with libpq-devel.
# postgresql-server-devel is required to compile server extension
%if 0%{?fedora} && 0%{?fedora} < 35
BuildRequires:  libpq-devel
%endif

# openssl is required for ssl-self-signed option in pg_auto_failover
Recommends:     openssl
Requires:       postgresql-server postgresql-contrib


%if %{with docs}
%package docs
Summary:        Extra documentation for pg_auto_failover
# Additional licenses for jQuery and other .js files
License:        ASL 1.0 and MIT and BSD
Requires:       %{name} = %precise_version
BuildArch:      noarch
%endif

%if %{with llvmjit}
%package llvmjit
Summary:        Just-in-time compilation support for pg_auto_failover
License:        ASL 1.0
Requires:       %{name}%{?_isa} = %precise_version
Requires:       postgresql-llvmjit
%endif

%description
pg_auto_failover is an extension and service for PostgreSQL that monitors and
manages automated failover for a Postgres cluster. It is optimized for
simplicity and correctness and supports Postgres 10 and newer.
We set up one PostgreSQL server as a monitor node as well as a primary and
secondary node for storing data. The monitor node tracks the health of the
data nodes and implements a failover state machine. On the PostgreSQL nodes,
the pg_autoctl program runs alongside PostgreSQL and runs the necessary
commands to configure synchronous streaming replication.

%if %{with docs}
%description docs
The pg_auto_failover-docs package contains some additional documentation for
pg_auto_failover. Currently, this includes the main documentation in HTML
format.
%endif

%if %{with llvmjit}
%description llvmjit
This packages provides JIT support for pg_auto_failover.
%endif

%prep
%autosetup -n %{name}-%{version} -p2

%build
# Generate additionally man/doc files
/usr/bin/make -O -j8 V=1 VERBOSE=1
/usr/bin/make man docs 

%install
%make_install

# man files are generated with white spaces in filenames
# brp-compress responsible for automatically compressing
# man pages won't detect them
for f in docs/_build/man/*\ *; do
    %{__mv} "$f" "${f// /_}";
done

%if %{without llvmjit}
%{__rm} -r %{buildroot}/%{_libdir}/pgsql/bitcode
%endif

# Add man files
install -p -D -m 0644 docs/_build/man/*.1 -t %{buildroot}%{_mandir}/man1
install -p -D -m 0644 docs/_build/man/*.5 -t %{buildroot}%{_mandir}/man5

%files
%{_bindir}/pg_autoctl
%{_libdir}/pgsql/pgautofailover.so
%{_datadir}/pgsql/extension/pgautofailover*.{sql,control}
%{_mandir}/man{1,5}/pg_auto*.{1,5}*
%license LICENSE

%if %{with docs}
%files docs
%doc docs/_build/html/* {README,CHANGELOG}.md
%endif

%if %{with llvmjit}
%files llvmjit
%dir %{_libdir}/pgsql/bitcode/pgautofailover
%{_libdir}/pgsql/bitcode/pgautofailover/*.bc
%{_libdir}/pgsql/bitcode/pgautofailover.index.bc
%endif

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 26 2023 Ondřej Sloup <osloup@redhat.com> - 2.0-0-1
- Rebase to the newest version
- Fix compatibility with PostgreSQL 15
- Remove patches as they are merged in upstream
- Use autosetup
- Manually build the package for documentation

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Ondřej Sloup <osloup@redhat.com> - 1.6.3-6
- Rebuild for new PostgreSQL 15

* Thu Aug 04 2022 Ondrej Sloup <osloup@redhat.com> - 1.6.3-5
- Add patch to fix format arguments in mvprintw (watch.c)
- Add lz4-devel as build requirement

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Filip Januš <fjanus@redhat.com> - 1.6.3-2
- Rebuild for Postgresql 14

* Wed Nov 24 2021 Marek Kulik <mkulik@redhat.com> 1.6.3-1
- Update to 1.6.3

* Sun Aug 22 2021 Marek Kulik <mkulik@redhat.com> 1.6.2-1
- Remove ISA requirement from docs package
- Initial build
