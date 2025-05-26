Name:           python-autograd
Version:        1.8.0
Release:        %autorelease
Summary:        Efficiently computes derivatives of numpy code

%global forgeurl https://github.com/HIPS/autograd
%forgemeta

# SPDX
License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist tomcli}

%global _description %{expand:
Autograd can automatically differentiate native Python and Numpy code. It can
handle a large subset of Python's features, including loops, ifs, recursion and
closures, and it can even take derivatives of derivatives of derivatives.  It
supports reverse-mode differentiation (a.k.a. backpropagation), which means it
can efficiently take gradients of scalar-valued functions with respect to
array-valued arguments, as well as forward-mode differentiation, and the two
can be composed arbitrarily. The main intended application of Autograd is
gradient-based optimization.}

%description %_description

%package -n python3-autograd
Summary:        %{summary}
Recommends:     python3-autograd+scipy

%description -n python3-autograd %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%pyproject_extras_subpkg -n python3-autograd scipy


%prep
%forgeautosetup -p1

# Remove pytest-cov and related options
tomcli set pyproject.toml \
    arrays delitem project.optional-dependencies.test pytest-cov
# Remove `tool.pytest.ini_options` entirely since most options are
# related to coverage. We set our own options in %%check.
tomcli set pyproject.toml \
    del tool.pytest.ini_options


%generate_buildrequires
%pyproject_buildrequires -x scipy,test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files autograd


%check
%pytest -r fEs


%files -n python3-autograd -f %{pyproject_files}
%license license.txt
%doc README.md docs/tutorial.md


%files doc
%doc examples/
%license license.txt


%changelog
%autochangelog
