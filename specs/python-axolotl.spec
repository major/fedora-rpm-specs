Name:           python-axolotl
Version:        0.2.3
Release:        %autorelease
Summary:        Python port of libaxolotl

License:        GPL-3.0-only
URL:            https://github.com/tgalal/python-axolotl
Source0:        %{url}/archive/%{version}/%{version}.tar.gz

# The protobuf dependency is too strict, this patch relaxes the requirement
# https://github.com/tgalal/python-axolotl/issues/44
Patch0:         python-axolotl-protobuf.patch
Patch1:         python-axolotl-remove-nose.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  protobuf-compiler

%global _description %{expand:
This is a ratcheting forward secrecy protocol
that works in synchronous and asynchronous messaging environments.}

%description %_description

%package -n python3-axolotl
Summary:        %{summary}

%description -n python3-axolotl %_description


%prep
%autosetup -p1

# Regenerate python protobuf files with system protoc to avoid compatibility issues with newer protobuf versions
cp axolotl/protobuf/LocalStorageProtocol.proto axolotl/protobuf/storageprotos.proto
cp axolotl/protobuf/WhisperTextProtocol.proto axolotl/protobuf/whisperprotos.proto
protoc --proto_path=axolotl/protobuf --python_out=axolotl/state storageprotos.proto
protoc --proto_path=axolotl/protobuf --python_out=axolotl/protocol whisperprotos.proto

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files axolotl


%check
%tox


%files -n python3-axolotl -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
%autochangelog
