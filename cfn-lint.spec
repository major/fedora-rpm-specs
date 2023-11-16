Name:           cfn-lint
Summary:        CloudFormation Linter
Version:        0.83.2
Release:        %autorelease

# SPDX
License:        MIT-0
URL:            https://github.com/aws-cloudformation/cfn-lint
# While the PyPI sdist contains the tests since 0.76.0, we still need data and
# documentation files that are only available in the GitHub archive.
Source0:        %{url}/archive/v%{version}/cfn-lint-%{version}.tar.gz
# Man page written for Fedora in groff_man(7) format based on --help output
Source1:        cfn-lint.1

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

# Graph generation requires either pygraphviz or pydot; tests expect the
# latter, but the former is preferred when both are installed.
BuildRequires:  python3dist(pydot)
Requires:       (python3dist(pygraphviz) or python3dist(pydot))

BuildRequires:  hardlink

BuildRequires:  python3dist(pytest)

# One function in cfnlint.maintenance calls “git grep”. It’s not entirely clear
# if this is really usable in a system-wide installation or not; it might be
# trying to operate on a git checkout of cfn-lint, which won’t be available. It
# doesn’t work for that reason when tested in
# TestUpdateDocumentation.test_update_docs, which is why there is no
# corresponding BuildRequires.
Recommends:     git-core

%py_provides python3-cfn-lint

%description
Validate AWS CloudFormation yaml/json templates against the AWS CloudFormation
Resource Specification and additional checks. Includes checking valid values
for resource properties and best practices.


%prep
%autosetup


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# This saves, as of this writing, roughly 250kB in duplicate data files and
# __init__.py files. Note that we do not pass “-t” because we do not want to
# ignore or discard differences in mtime. Note also that rpmlint will complain
# about cross-directory hardlinks, but that these are not a problem because the
# contents of a directory owned by this package are guaranteed to be on a
# single filesystem.
hardlink '%{buildroot}%{python3_sitelib}/cfnlint'
%pyproject_save_files cfnlint
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'


%check
# These tests want to make HTTP(S) requests to the Internet:
k="${k-}${k+ and }not (TestFormatters and test_sarif_formatter)"
k="${k-}${k+ and }not (TestUpdateResourceSpecs and test_update_resource_specs_python_2)"
k="${k-}${k+ and }not (TestUpdateResourceSpecs and test_update_resource_specs_python_3)"

# This test tries to use “git grep”, but there is no git repository.
k="${k-}${k+ and }not (TestUpdateDocumentation and test_update_docs)"

# Tests fail if we parallelize with pytest-xdist… so don’t do that!
#
# LANG and AWS_DEFAULT_REGION are set as they are in tox.ini.
#
# We skip the TestCli tests the first time, then run them separately; they fail
# with the wrong region if run together with the other tests. This is probably
# a mocking issue. It doesn’t seem to be a problem when using unittest as the
# runner, as upstream does, but that would make it hard for us to skip tests
# (e.g. because they need network access).
k="${k-}${k+ and }not TestCli"
LANG=en_US.UTF-8 AWS_DEFAULT_REGION=us-east-1 %pytest -k "${k-}"
LANG=en_US.UTF-8 AWS_DEFAULT_REGION=us-east-1 %pytest -k 'TestCli'


%files -f %{pyproject_files}
# pyproject-rpm-macros handles LICENSE and NOTICE (verify with “rpm -qL -p …”)

# We don’t provide a separate documentation package since all of the following
# documentation is still not very big. As of this writing, it totals ~250kB
# extracted and a couple dozen files, in the context of a base package that is
# >100MB extracted with around a thousand files.
%doc CHANGELOG.md
%doc README.md
# Markdown
%doc docs/
%doc examples/

%{_bindir}/cfn-lint
%{_mandir}/man1/cfn-lint.1*


%changelog
%autochangelog
