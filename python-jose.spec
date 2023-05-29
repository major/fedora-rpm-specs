# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-jose
Version:        3.3.0
Release:        %autorelease
Summary:        A JOSE implementation in Python

# SPDX
License:        MIT
URL:            https://github.com/mpdavis/python-jose
Source:         %{pypi_source python-jose}

BuildArch:      noarch

BuildRequires:  python3-devel

# From setup_requires:
BuildRequires:  python3dist(pytest-runner)

# Documentation
%if %{with doc_pdf}
BuildRequires:  make
# From requirements-rtd.txt:
# sphinxcontrib-napoleon==0.3.4; but napoleon is now part of Sphinx proper
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  tex-xetex-bin
%endif

# Upstream recommends the cryptography backend. We add it as a soft dependency
# so that anyone who does not go out of their way to select a different backend
# gets the best experience.
Recommends:     python3dist(python-jose[cryptography])

%global common_description %{expand:
The JavaScript Object Signing and Encryption (JOSE) technologies - JSON Web
Signature (JWS), JSON Web Encryption (JWE), JSON Web Key (JWK), and JSON Web
Algorithms (JWA) - collectively can be used to encrypt and/or sign content
using a variety of algorithms. While the full set of permutations is extremely
large, and might be daunting to some, it is expected that most applications
will only use a small set of algorithms to meet their needs.

As of 3.3.0, python-jose implements three different cryptographic backends. The
backend must be selected as an extra when installing python-jose. If you do not
select a backend, the native-python backend will be installed.

Unless otherwise noted, all backends support all operations.

Due to complexities with setuptools, the native-python backend is always
installed, even if you select a different backend on install.

  1. cryptography
       * This backend uses pyca/cryptography for all cryptographic operations.
         This is the recommended backend and is selected over all other
         backends if any others are present.
       * Installation: dnf install python3-jose+cryptography
       * Unused dependencies:
           - rsa
           - ecdsa
           - pyasn1

  2. pycryptodome
       * This backend uses pycryptodome for all cryptographic operations.
       * Installation: not available because pycryptodome (which, unlike
                       pycryptodomex, conflicts with pycrypto) is not packaged
       * Unused dependencies:
           - rsa

  3. native-python
       * This backend uses python-rsa and python-ecdsa for all cryptographic
         operations. This backend is always installed but any other backend
         will take precedence if one is installed.
       * Installation: dnf install python3-jose

     Note

     The native-python backend cannot process certificates.}

%description %{common_description}


%package -n     python3-jose
Summary:        %{summary}

%description -n python3-jose %{common_description}


# Fedora packages pycryptodomex, but not pycryptodome (which conflicts with
# pycrypto). Upstream refuses to switch to pycryptodomex for the pycryptodome
# backend (https://github.com/mpdavis/python-jose/issues/26), so we disable the
# corresponding extra because it will fail to install.
%pyproject_extras_subpkg -n python3-jose cryptography


%package doc
Summary:        Documentation for python-jose

%description doc %{common_description}


%prep
%autosetup -p1

# Patch out pycryptodome backend extra and tests where required; see note near
# the BR’s
sed -r -i '/^[[:blank:]]*pycryptodome/d' tox.ini requirements.txt

# The napoleon extension is now part of Sphinx proper:
sed -r -i 's/(sphinx)contrib(\.napoleon)/\1.ext\2/g' docs/conf.py

# Patch out unnecessary coverage dependencies:
sed -r -i '/pytest-cov/d' tox.ini


%generate_buildrequires
%pyproject_buildrequires -t -x cryptography


%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files jose


%check
echo '>>> Backend: native-python <<<' 1>&2
m='not (cryptography or pycryptodome or backend_compatibility)'
%{pytest} -k "${k}" -m "${m}" tests

echo '>>> Backend: cryptography <<<' 1>&2
m='not (pycryptodome or backend_compatibility)'
%{pytest} -k "${k}" -m "${m}" tests

echo '>>> Cross-backend compatibility and coexistence <<<' 1>&2
%{pytest} -k "${k}" tests


%files -n python3-jose -f %{pyproject_files}
%doc README.rst


%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/python-jose.pdf
%endif


%changelog
%autochangelog
