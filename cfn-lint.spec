Name:           cfn-lint
Summary:        CloudFormation Linter
Version:        0.72.9
Release:        %autorelease

# SPDX
License:        MIT-0
URL:            https://github.com/aws-cloudformation/cfn-lint
Source0:        %{url}/archive/v%{version}/cfn-lint-%{version}.tar.gz
# Man page written for Fedora in groff_man(7) format based on --help output
Source1:        cfn-lint.1

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

# Graph generation requires either pygraphviz or pydot; only the former is
# packaged, and it is preferred when both are available anyway.
BuildRequires:  python3dist(pygraphviz)
Requires:       python3dist(pygraphviz)

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
# The checks on the graphviz/dot output appear to be excessively dependent on a
# particular version of pygraphviz:
#
#   >               assert len(file_contents) == len(expected_content) and
#                   sorted(file_contents) == sorted(expected_content)
#   E               AssertionError: assert (25 == 19)
#   E                +  where 25 = len(['digraph template {', ...])
#   E                +  and   19 = len(['digraph "template" {', ...])
k="${k-}${k+ and }not (TestTemplate and test_build_graph)"

# These tests want to make HTTP(S) requests to the Internet:
k="${k-}${k+ and }not (TestFormatters and test_sarif_formatter)"
k="${k-}${k+ and }not (TestUpdateResourceSpecs and test_update_resource_specs_python_2)"
k="${k-}${k+ and }not (TestUpdateResourceSpecs and test_update_resource_specs_python_3)"

# This test tries to use “git grep”, but there is no git repository.
k="${k-}${k+ and }not (TestUpdateDocumentation and test_update_docs)"

# Tests fail if we parallelize with pytest-xdist… so don’t do that!
%pytest -k "${k-}"


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
