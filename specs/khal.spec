# Invoke with "--with tests" to enable tests
# Currently disabled by default as it requires network by default
%bcond_with tests

Name:       khal
Version:    0.11.3
Release:    %autorelease
Summary:    CLI calendar application

License:    MIT
URL:        https://github.com/pimutils/%{name}
Source0:    https://files.pythonhosted.org/packages/source/k/%{name}/%{name}-%{version}.tar.gz

# In theory documentation requires sphinxcontrib.newsfeed to generate
# a blog of the changelog. We only need the manpage. We also fix a Makefile error
# which happens when using .tar.gz
Patch0:     khal-0.8.2-sphinx-docfix.patch
# https://github.com/pimutils/khal/pull/1365
Patch1:     khal-0.11.3-intersphinx-fix.patch
BuildArch:  noarch

BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

Requires:       python3-click >= 3.2
Requires:       python3-configobj
Requires:       python3-dateutil
Requires:       python3-icalendar
Requires:       python3-urwid
Requires:       python3-tzlocal
Requires:       python3-pytz
Requires:       python3-pyxdg
Requires:       vdirsyncer >= 0.8.1-2

%description
Khal is a standards based CLI (console) calendar program. CalDAV compatibility
is achieved by using vdir/vdirsyncer as a back-end, allowing syncing of
calendars with a variety of other programs on a host of different platforms.

%prep
%autosetup -p1 -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel
cd doc
# Not using _smp_flags as sphinx barfs with it from time to time
PYTHONPATH=.. make SPHINXBUILD=sphinx-build-3 man html text
cd ..

%install
%pyproject_install
%pyproject_save_files khal
# separately install man pages
install -d "$RPM_BUILD_ROOT%{_mandir}/man1"
cp -r doc/build/man/%{name}.1 "$RPM_BUILD_ROOT%{_mandir}/man1"
# Remove extra copy of text docs
rm -vrf doc/build/html/_sources
rm -fv doc/build/html/{.buildinfo,objects.inv}

%check
# needs python3-tox bz #1010767
%if %{with tests}
%tox
%endif


%files -f %{pyproject_files}
%doc AUTHORS.txt README.rst CONTRIBUTING.rst khal.conf.sample doc/build/html doc/build/text
%license COPYING
%{_bindir}/ikhal
%{_bindir}/khal
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
