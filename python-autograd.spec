# Why not use forge macros when pulling from GitHub
%global forgeurl https://github.com/HIPS/autograd

# We’re using a git commit because the PyPI tar does not contain any tests but
# the github source does; unfortunately, upstream does not tag releases on
# GitHub, but we are confident we are using the git commit that corresponds to
# the PyPI release.
# https://github.com/HIPS/autograd/issues/392
%global commit 1bb5cbc21d2aa06e0c61654a9cc6f38c174dacc0

# Don't use commit in dist tag
%global distprefix %{nil}

Name:           python-autograd
# Because we are using the commit that corresponds to the PyPI release (even
# though it is not tagged), we do not use the snapinfo version field even
# though our source URL is based on the git commit hash.
Version:        1.6.2
Release:        %autorelease
Summary:        Efficiently computes derivatives of numpy code
%forgemeta
# SPDX
License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-scipy

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

Recommends:     python3-scipy

%description -n python3-autograd %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files autograd


%check
%pyproject_check_import

# https://github.com/HIPS/autograd/issues/588#issuecomment-1479446916
k="${k-}${k+ and }not test_odeint"

%pytest -k "${k-}"


%files -n python3-autograd -f %{pyproject_files}
%doc README.md


%files doc
%doc examples/
%license license.txt


%changelog
%autochangelog
