%global         pypi_name       tinygrad
%global         forgeurl        https://github.com/tinygrad/tinygrad
Version:        0.12.0
%forgemeta

Name:           python-%{pypi_name}
Release:        1%{?dist}
Summary:        You like pytorch? You like micrograd? You'll love tinygrad!

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  python3-devel
BuildRequires:  gcc
# Needed for test
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(hypothesis)
BuildArch: noarch

%global common_description %{expand:
tinygrad: For something between PyTorch and karpathy/micrograd. Maintained
by tiny corp.

This may not be the best deep learning framework, but it is a deep learning
framework.

Due to its extreme simplicity, it aims to be the easiest framework to add new
accelerators to, with support for both inference and training. If XLA is CISC,
tinygrad is RISC.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%package  -n python3-%{pypi_name}-examples
Summary:  Examples for tinygrad
Requires: %{name} = %{version}-%{release}
Requires: python3-tiktoken
Requires: python3-pyopencl
Requires: clang

%description -n python3-%{pypi_name}-examples
Examples for tinygrad

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
%py3_check_import %{pypi_name}
# Run CPU tests that do not need dependencies not in Fedora
# Modified from
# https://github.com/tinygrad/tinygrad/blob/master/.github/workflows/test.yml
# Tests only run on these arches
%ifarch aarch64 x86_64
PYTHON=1 SKIP_SLOW_TEST=1 %python3 -m pytest \
          test/test_assign.py \
          test/test_dtype_alu.py \
          test/test_gc.py \
          test/test_graph.py \
          test/test_jit.py \
          test/test_linearizer.py \
          test/test_multitensor.py \
          test/test_symbolic_jit.py \
          test/test_symbolic_ops.py \
          test/test_uops.py \
          test/unit/test_conv.py \
          %{nil}
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc docs/quickstart.md docs/env_vars.md docs/mnist.md docs/runtime.md
%doc docs/*pdf docs/showcase.md docs/*svg
%doc docs/developer/ docs/showcase/ docs/tensor/
%doc docs/abstractions*.py

%files -n python3-%{pypi_name}-examples
%doc examples

%changelog
* Tue Jan 13 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 0.12.0-1
- Update to 0.12.0
- Include examples sub package

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 0.7.0-9
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.7.0-8
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Python Maint <python-maint@redhat.com> - 0.7.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 02 2023 Benson Muite <benson_muite@emailplus.org> - 0.7.0-1
- Initial package
