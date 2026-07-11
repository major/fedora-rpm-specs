# Invoke with "--with tests" to enable tests
# Currently disabled by default as it requires network by default
%bcond_with tests

Name:       khal
Version:    0.14.0
Release:    %autorelease
Summary:    CLI calendar application

License:    MIT
URL:        https://github.com/pimutils/%{name}
Source:     https://files.pythonhosted.org/packages/source/k/%{name}/%{name}-%{version}.tar.gz

# In theory documentation requires sphinxcontrib.newsfeed to generate
# a blog of the changelog. We only need the manpage.
Patch:      0001-remove-sphinxfeed.patch
BuildArch:  noarch

BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

Requires:       vdirsyncer >= 0.8.1-2

%description
Khal is a standards based CLI (console) calendar program. CalDAV compatibility
is achieved by using vdir/vdirsyncer as a back-end, allowing syncing of
calendars with a variety of other programs on a host of different platforms.

%prep
%autosetup -p1 -n %{name}-%{version}

# Don't limit the upper bound of the required Python
# Enables testing in Fedora with 3.15 alpha versions
sed -i 's/^\(requires-python *= *">=[^"]*\),<3\.15"/\1"/' pyproject.toml

%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -t
%else
%pyproject_buildrequires
%endif

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
install -d "%{buildroot}%{_mandir}/man1"
cp -r doc/build/man/%{name}.1 "%{buildroot}%{_mandir}/man1"
# Remove extra copy of text docs
rm -vrf doc/build/html/_sources
rm -fv doc/build/html/{.buildinfo,objects.inv}

# Generate and install shell completions
install -d %{buildroot}%{bash_completions_dir}
install -d %{buildroot}%{fish_completions_dir}
install -d %{buildroot}%{zsh_completions_dir}

PYTHONPATH=%{buildroot}%{python3_sitelib} \
    _KHAL_COMPLETE=bash_source \
    %{buildroot}%{_bindir}/khal > %{buildroot}%{bash_completions_dir}/khal
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    _IKHAL_COMPLETE=bash_source \
    %{buildroot}%{_bindir}/ikhal > %{buildroot}%{bash_completions_dir}/ikhal

PYTHONPATH=%{buildroot}%{python3_sitelib} \
    _KHAL_COMPLETE=fish_source \
    %{buildroot}%{_bindir}/khal > %{buildroot}%{fish_completions_dir}/khal.fish
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    _IKHAL_COMPLETE=fish_source \
    %{buildroot}%{_bindir}/ikhal > %{buildroot}%{fish_completions_dir}/ikhal.fish

PYTHONPATH=%{buildroot}%{python3_sitelib} \
    _KHAL_COMPLETE=zsh_source \
    %{buildroot}%{_bindir}/khal > %{buildroot}%{zsh_completions_dir}/_khal
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    _IKHAL_COMPLETE=zsh_source \
    %{buildroot}%{_bindir}/ikhal > %{buildroot}%{zsh_completions_dir}/_ikhal

%check
%pyproject_check_import

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
%{bash_completions_dir}/khal
%{bash_completions_dir}/ikhal
%{fish_completions_dir}/khal.fish
%{fish_completions_dir}/ikhal.fish
%{zsh_completions_dir}/_khal
%{zsh_completions_dir}/_ikhal

%changelog
%autochangelog
