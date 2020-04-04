import porespy as ps


def generate_porous_structure():
    return ps.generators.blobs(shape=[100, 100, 100], porosity=0.7, blobiness=1)


def main():
    structure = generate_porous_structure()
    print(structure.shape)


if __name__ == '__main__':
    main()
