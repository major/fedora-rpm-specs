Name:           python-cucumber-tag-expressions
Version:        10.0.0
Release:        %autorelease
Summary:        Provides a tag-expression parser and evaluation logic for cucumber/behave

License:        MIT
URL:            https://github.com/cucumber/tag-expressions
# The GitHub archive has test data files; the PyPI sdist does not.
Source:         %{url}/archive/v%{version}/tag-expressions-%{version}.tar.gz

BuildSystem:    pyproject
BuildOption(generate_buildrequires): --directory python
BuildOption(build): --directory python
BuildOption(install): --assert-license cucumber_tag_expressions

BuildArch:      noarch

# Test dependencies are intermixed with unwanted linting and coverage-analysis
# tools in the “dev” dependency group, so we enumerate them manually.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  %{py3_dist pytest} >= 6.0.1
BuildRequires:  %{py3_dist pyyaml} >= 6.0.3

%global common_description %{expand:
Cucumber tag-expressions provide readable boolean expressions to select
features and scenarios marked with tags in Gherkin files in an easy way.}

%description %{common_description}


%package -n python3-cucumber-tag-expressions
Summary:        %{summary}

%description -n python3-cucumber-tag-expressions %{common_description}


%prep -a
# We must work with what we have, and compatibility is quite good in practice.
%pyproject_patch_dependency uv_build:drop_upper


%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%install -p
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_pkgdocdir}/general' \
    ARCHITECTURE.md CHANGELOG.md README.md
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_pkgdocdir}' python/README.md


%check -a
%pytest python/tests --verbose


%files -n python3-cucumber-tag-expressions -f %{pyproject_files}
%doc %{_pkgdocdir}/


%changelog
%autochangelog
