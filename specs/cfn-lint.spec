Name:           cfn-lint
Summary:        CloudFormation Linter
Version:        1.22.4
Release:        %autorelease

# The entire source is MIT-0, except that some sources are derived from
# jsonschema https://pypi.org/project/jsonschema/, which is under an MIT
# license; the copyright and license notice is reproduced in the sources:
#   - src/cfnlint/jsonschema/_format.py
#   - src/cfnlint/jsonschema/_keywords.py
#   - src/cfnlint/jsonschema/_keywords_cfn.py
#   - src/cfnlint/jsonschema/_types.py
#   - src/cfnlint/jsonschema/_typing.py
#   - src/cfnlint/jsonschema/_utils.py
#   - src/cfnlint/jsonschema/exceptions.py
#   - src/cfnlint/jsonschema/protocols.py
#   - src/cfnlint/jsonschema/validators.py
#   - src/cfnlint/schema/resolver/_exceptions.py
#   - src/cfnlint/schema/resolver/_resolver.py
#   - src/cfnlint/schema/resolver/_utils.py
License:        MIT-0 AND MIT
# Additionally, two test files are Apache-2.0, but these are not included in
# the binary RPMs:
#   - test/fixtures/templates/quickstart/openshift.yaml
#   - test/fixtures/templates/quickstart/openshift_master.yaml
SourceLicense:  %{license} AND Apache-2.0
URL:            https://github.com/aws-cloudformation/cfn-lint
# While the PyPI sdist contains the tests since 0.76.0, we still need data and
# documentation files that are only available in the GitHub archive.
Source0:        %{url}/archive/v%{version}/cfn-lint-%{version}.tar.gz
# Man page written for Fedora in groff_man(7) format based on --help output
Source1:        cfn-lint.1

BuildSystem:            pyproject
BuildOption(install):   -l cfnlint
BuildOption(generate_buildrequires): -x full,graph,junit,sarif

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  hardlink

# From tox.ini:
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist defusedxml}

# One function in cfnlint.maintenance calls “git grep”. It’s not entirely clear
# if this is really usable in a system-wide installation or not; it might be
# trying to operate on a git checkout of cfn-lint, which won’t be available. It
# doesn’t work for that reason when tested in
# TestUpdateDocumentation.test_update_docs, which is why there is no
# corresponding BuildRequires.
Recommends:     git-core

# Since this is an application rather than a library, we choose to carry weak
# dependencies on the extras so that users have access to all features by
# default.
Recommends:     cfn-lint+graph = %{version}-%{release}
Recommends:     cfn-lint+junit = %{version}-%{release}
Recommends:     cfn-lint+sarif = %{version}-%{release}

%py_provides python3-cfn-lint

# A number of files are forked from https://pypi.org/project/jsonschema/; see
# the comment above License for a list of these files.
Provides:       bundled(python3dist(jsonschema))

%description
Validate AWS CloudFormation yaml/json templates against the AWS CloudFormation
Resource Specification and additional checks. Includes checking valid values
for resource properties and best practices.


%pyproject_extras_subpkg -n cfn-lint full graph junit sarif


%install -a
# This saves, as of this writing, over 4 MiB in duplicate data files and
# __init__.py files. Because timestamp differences across source files are not
# meaningful (are not really properties of the individual files), and all
# timestamps are *nearly* the same, we elect to pass “-t” in order to hardlink
# more duplicate files, in exchange for ignoring/discarding these insignificant
# timestamp differences.  single filesystem.
hardlink -t '%{buildroot}%{python3_sitelib}/cfnlint'
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'


%check -a
# These tests want to make HTTP(S) requests to the Internet:
k="${k-}${k+ and }not (TestFormatters and test_sarif_formatter)"
k="${k-}${k+ and }not (TestUpdateResourceSpecs and test_update_resource_specs_python_2)"
k="${k-}${k+ and }not (TestUpdateResourceSpecs and test_update_resource_specs_python_3)"

# This test tries to use “git grep”, but there is no git repository.
k="${k-}${k+ and }not (TestUpdateDocumentation and test_update_docs)"

# This test expects graphviz/dot output to be identical, down to the order of
# properties, which is not a portable expectation.
k="${k-}${k+ and }not (TestTemplate and test_build_graph)"

# Tests fail if we parallelize with pytest-xdist… so don’t do that!
#
# LANG and AWS_DEFAULT_REGION are set as they are in tox.ini.
LANG=en_US.UTF-8 AWS_DEFAULT_REGION=us-east-1 %pytest -k "${k-}"


%files -f %{pyproject_files}
# We don’t provide a separate documentation package since all of the following
# documentation is still not very big. As of this writing, it totals ~325kB
# extracted and a couple dozen files, in the context of a base package that is
# >15MB extracted with several thousand files.
%doc CHANGELOG.md
%doc README.md
# Markdown
%doc docs/
%doc examples/

%{_bindir}/cfn-lint
%{_mandir}/man1/cfn-lint.1*


%changelog
%autochangelog
