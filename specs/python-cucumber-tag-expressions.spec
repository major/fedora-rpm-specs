Name:           python-cucumber-tag-expressions
Version:        6.2.0
Release:        %autorelease
Summary:        Provides a tag-expression parser and evaluation logic for cucumber/behave

License:        MIT
URL:            https://github.com/cucumber/tag-expressions
# The GitHub archive has test data files; the PyPI sdist does not.
Source:         %{url}/archive/v%{version}/tag-expressions-%{version}.tar.gz

# Downstream-only: omit pytest options for pytest-html
# (We patch it out in %%prep because we do not need HTML reports.)
Patch:          0001-Downstream-only-omit-pytest-options-for-pytest-html.patch

BuildSystem:            pyproject
BuildOption(install):   -L cucumber_tag_expressions
BuildOption(generate_buildrequires): -x testing

BuildArch:      noarch

BuildRequires:  tomcli

%global common_description %{expand:
Cucumber tag-expressions provide readable boolean expressions to select
features and scenarios marked with tags in Gherkin files in an easy way.}

%description %{common_description}


%package -n python3-cucumber-tag-expressions
Summary:        %{summary}

%description -n python3-cucumber-tag-expressions %{common_description}


%prep -a
# We do not need HTML reports from pytest.
tomcli set python/pyproject.toml lists delitem \
    project.optional-dependencies.testing 'pytest-\bhtml.*'


%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
cd python


%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
cd python


%install -p
install -t '%{buildroot}%{_pkgdocdir}/general' -p -m 0644 -D \
    ARCHITECTURE.md CHANGELOG.md README.md
install -t '%{buildroot}%{_pkgdocdir}' -p -m 0644 -D python/README.rst


%check -a
%pytest python/tests -v


%files -n python3-cucumber-tag-expressions -f %{pyproject_files}
%license LICENSE
%doc %{_pkgdocdir}/


%changelog
%autochangelog
