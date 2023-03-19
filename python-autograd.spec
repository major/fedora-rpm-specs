#we're using a git commit because the pypi tar does not contain any tests but the github source does, the git commit that corresponds to the pypi release is being used
%global commit e12041cc230188342688fd7426e885fd7e7e9f48
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-autograd
Version:        1.3
Release:        %autorelease
Summary:        Efficiently computes derivatives of numpy code

License:        MIT
URL:            https://github.com/HIPS/autograd
Source0:        https://github.com/HIPS/autograd/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# Replace inspect.getargspec on Python 3
# https://github.com/HIPS/autograd/pull/578
Patch:          %{url}/pull/578.patch
# numpy 1.20.0 deprecates np.int, with 1.24 it seems removed
# https://github.com/HIPS/autograd/issues/565
# https://github.com/HIPS/autograd/commit/01eacff7a4f12e6f7aebde7c4cb4c1c2633f217d
Patch:          %{name}-01eacff7-rm-deprecated-np_int.patch

BuildArch:      noarch
BuildRequires:  python3-pytest
BuildRequires:  python3-devel

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

%description -n python3-autograd %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.


%prep
%autosetup -n autograd-%{commit} -p1

%generate_buildrequires
%pyproject_buildrequires -r



%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files autograd


%check
%pytest
%py3_check_import autograd


%files -n python3-autograd -f %{pyproject_files}
%doc README.md

%files doc
%doc examples
%license license.txt


%changelog
%autochangelog
