Name:           python-nose2
Version:        0.15.1
Release:        %autorelease
Summary:        The successor to nose, based on unittest2

# The entire source is BSD-2-Clause, except that unspecified portions are
# derived from unittest2 under a BSD-3-Clause. See LICENSE.
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://nose2.io/
%global forgeurl https://github.com/nose-devs/nose2
Source0:        %{forgeurl}/archive/%{version}/nose2-%{version}.tar.gz
# Man page written for Fedora in groff_man(7) format based on --help output
Source1:        nose2.1

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -e %{toxenv}-nocov
BuildOption(install):   -l nose2
# We remove nose2.tests from the buildroot in %%install.
BuildOption(check):     -e nose2.tests*

BuildArch:      noarch

BuildRequires:  tomcli

%global common_description %{expand:
nose2 is the successor to nose.

It’s unittest with plugins.

nose2’s purpose is to extend unittest to make testing nicer and easier to
understand.}

%description %{common_description}


%package -n python3-nose2
Summary:        %{summary}

# Removed for Fedora 43; we can remove the Obsoletes after Fedora 46.
Obsoletes:      python-nose2-doc < 0.15.1-9

%description -n python3-nose2 %{common_description}


%pyproject_extras_subpkg -n python3-nose2 coverage_plugin


%prep -a
# We are not building documentation.
tomcli set pyproject.toml lists delitem project.optional-dependencies.dev \
    'sphinx*'

# Remove shebangs from non-script sources. The find-then-modify pattern
# preserves mtimes on sources that did not need to be modified.
find nose2/ -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r -t sed -r -i '1{/^#!/d}'


%install -a
# Don’t install the tests; we are not sure how to fix this *successfully* in
# pyproject.toml, even after reading
# https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html#setuptools-specific-configuration,
# so we haven’t suggested any change upstream. Still, the tests are large and
# unlikely to be useful to package users.
rm -rvf '%{buildroot}%{python3_sitelib}/nose2/tests/'
sed -r -i '/\/nose2\/tests(\/|$)/d' %{pyproject_files}

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'


%check -a
%tox -e %{default_toxenv}-nocov


%files -n python3-nose2 -f %{pyproject_files}
%doc AUTHORS
%doc README.rst
%doc docs/changelog.rst

%{_bindir}/nose2
%{_mandir}/man1/nose2.1*


%changelog
%autochangelog
