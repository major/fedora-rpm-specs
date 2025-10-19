%global commit0 e9a4e7510c89613a2fe75312fba1fb8c14b3b376
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250727

Name:           pytorch-examples
Version:        0.0^git%{date0}.%{shortcommit0}
Release:        %autorelease
Summary:        PyTorch Examples

License:        BSD-3-Clause AND MIT
# The main license is BSD-3-Clause
# The few differences
#
# MIT
# mnist_forward_forward/main.py
# This code is based on the implementation of Mohammad Pezeshki available at
# https://github.com/mohammadpz/pytorch_forward_forward and licensed under the MIT License.
#
# distributed/FSDP/utils/environment.py
# Apache
# Copyright (c) 2022 Meta Platforms, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the Apache-style license found in the
# LICENSE file in the root directory of this source tree.
#
# Apache-style is not a real license, file this issue
# https://github.com/pytorch/examples/issues/1378

URL:            https://github.com/pytorch/examples
Source0:        %{url}/archive/%{commit0}/examples-%{shortcommit0}.tar.gz
Patch1:         0001-Fix-license-in-environment.py.patch

# Only samples
BuildArch:      noarch
ExclusiveArch:  aarch64 x86_64

BuildRequires:  fdupes

Requires:  python3dist(aiohttp)
Requires:  python3dist(boto3)
Requires:  python3dist(lmdb)
Requires:  python3dist(matplotlib)
Requires:  python3dist(numpy)
Requires:  python3dist(portalocker)
Requires:  python3dist(protobuf)
Requires:  python3dist(pygame)
Requires:  python3dist(requests)
Requires:  python3dist(sentencepiece)
Requires:  python3dist(six)
Requires:  python3dist(sphinx)
Requires:  python3dist(torch)
Requires:  python3dist(torchdata)
Requires:  python3dist(torchtext)
Requires:  python3dist(torchvision)
Requires:  python3dist(tqdm)

%description
pytorch-examples showcases examples of using PyTorch.  The goal
is to have curated, short, few/no dependencies high quality examples
that are substantially different from each other that can be
emulated in your existing work.

%prep
%autosetup -p1 -n examples-%{commit0}
# *** WARNING: .../distributed/ddp/run_example.sh is executable but has no shebang, removing executable bit
sed -i -e 's@# /bin/bash@#!/usr/bin/bash@' distributed/ddp/run_example.sh
# mangling shebang in .../distributed/minGPT-ddp/run_example.sh from /bin/bash to #!/usr/bin/bash
sed -i -e 's@#!/bin/bash@#!/usr/bin/bash@' distributed/minGPT-ddp/run_example.sh
# *** WARNING: .../distributed/tensor_parallelism/tensor_parallel_example.py is executable but has no shebang, removing executable bit
# Leave as-is
# *** ERROR: ambiguous python shebang in .../regression/main.py: #!/usr/bin/env python. Change it to python3 (or python2) explicitly.
sed -i -e 's@usr/bin/env python@usr/bin/python3@' regression/main.py

# Remove some cruft rpmlint found
# pytorch-examples.noarch: E: zero-length /usr/share/pytorch-examples/docs/source/_static/.gitkeep
find . -name .gitkeep -type f -delete
# pytorch-examples.noarch: E: version-control-internal-file /usr/share/pytorch-examples/.gitignore
find . -name .gitignore -type f -delete
# pytorch-examples.noarch: W: hidden-file-or-dir /usr/share/pytorch-examples/.github
rm -rf .github
# pytorch-examples.noarch: W: hidden-file-or-dir /usr/share/pytorch-examples/cpp/.clang-format
find . -name .clang-format -type f -delete

# Fix some premissions
for f in `find . -name '*.sh'`; do
    chmod 755 $f
    sed -i -e 's@/usr/bin/env bash@/usr/bin/bash@' $f
done
for f in `find . -name '*.py'`; do
    sed -i -e 's@/usr/bin/env python3@/usr/bin/python3@' $f
done
chmod 755 docs/source/conf.py

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -p -r . %{buildroot}%{_datadir}/%{name}

# Extra docs
rm %{buildroot}%{_datadir}/%{name}/README.md
rm %{buildroot}%{_datadir}/%{name}/LICENSE

# Take care of dupes
# Causes these warnings
# pytorch-examples.noarch: W: cross-directory-hard-link /usr/share/pytorch-examples/mnist_forward_forward/requirements.txt /usr/share/pytorch-examples/fx/requirements.txt
%fdupes %{buildroot}%{_datadir}/%{name}

%files
%doc README.md
%license LICENSE
%{_datadir}/%{name}/

%changelog
%autochangelog
