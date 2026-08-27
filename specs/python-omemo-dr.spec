Name:           python-omemo-dr
Version:        1.2.0
Release:        %autorelease
Summary:        OMEMO Double Ratchet

License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            https://pypi.org/project/omemo-dr/
# Need sources with protobuf source files which are
# not included in the PyPI archive
Source:         https://dev.gajim.org/gajim/omemo-dr/-/archive/v%{version}/omemo-dr-v%{version}.tar.gz

# Regenerate protoc files
BuildRequires:  protobuf-compiler
BuildRequires:  gcc
# Tests
BuildRequires:  python3dist(pytest)
# At least curve25519/curve/curve25519-donna.c and
# curve25519/curve25519module.c are from
# https://code.google.com/archive/p/curve25519-donna/ /
# https://github.com/agl/curve25519-donna, corresponding to
# https://pypi.org/project/curve25519-donna/.
#
# Issue to see if code can be unbundled
# https://bugzilla.redhat.com/show_bug.cgi?id=2440337
Provides:       bundled(python3dist(curve25519-donna))

%global _description %{expand:
This library handles only the crypto part of OMEMO, not the XMPP protocol part.
This means you need to take care yourself of things like publishing/downloading
bundles, publishing/subscribing to PEP deviceliste updates, sending and
receiving messages.}

%description %_description

%package -n     python3-omemo-dr
Summary:        %{summary}


%description -n python3-omemo-dr %_description



%prep
%autosetup -p1 -n omemo-dr-v%{version}
# Relax protobuf version dependency
sed -i "s/protobuf>=4.21.0/protobuf/g" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
# Regenerate protobuf files
protoc -I=src/omemo_dr/protobuf --python_out=src/omemo_dr/protocol omemo.proto whisper.proto
protoc -I=src/omemo_dr/protobuf --python_out=src/omemo_dr/state storage.proto

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l omemo_dr


%check
%pyproject_check_import
%pytest

%files -n python3-omemo-dr -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md

%changelog
%autochangelog
