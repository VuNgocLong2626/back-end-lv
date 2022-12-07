from app.models.schemas import neighbour as _neighbour_schemas
from app.db.entity import neighbour as _neighbour
from app.utils import dfs as _dfs
import ast
import time

from app.db.neighbour import neighbourRepositories


_repo = neighbourRepositories()


class neighbourService():

    # tạo đường sẽ tạo chung
    def create_neighbour(neighbour_in: _neighbour_schemas.NeighbourIn):
        neighbour = _neighbour.neighbourEtity(
            **neighbour_in.dict(by_alias=True)
        )
        neighbour.number_neighbour = len(_repo.get_all_neighbour()) + 1
        _ = _repo.create_neighbour(neighbour.dict(by_alias=True))
        return {'message': 'create successfully'}

    def get_all_neighbour():
        response = _repo.get_all_neighbour()
        t = sorted(response, key=lambda d: d['NumberNeighbour'])
        return t

    def delete_neighbour(neighbour_in: _neighbour_schemas.NeighbourIn):
        neighbour = _neighbour.neighbourEtity(
            **neighbour_in.dict(by_alias=True)
        )
        _ = _repo.delete_neighbour(neighbour.pk, neighbour.sk)
        return {'message': 'delete successfully'}

    def update_list_address(data_in: _neighbour_schemas.NeighbourUpdateListAddress):
        neighbour = _repo.get_neighbour(
            f'NEIGHBOUR#{data_in.id_space_neighbour}',
            f'NEIGHBOUR#{data_in.id_space_neighbour}')
        current = _repo.get_neighbour(
            f'NEIGHBOUR#{data_in.id_space_current}',
            f'NEIGHBOUR#{data_in.id_space_current}')
        list_address = neighbour.get('ListAddressNeighbour').copy()
        list_address.append(
            current.get('NumberNeighbour'))
        _ = _repo.update_list_address(
            f'NEIGHBOUR#{data_in.id_space_neighbour}',
            f'NEIGHBOUR#{data_in.id_space_neighbour}',
            list_address
        )
        return {'message': 'update successfully'}

    def update_list_location(data_in: _neighbour_schemas.NeighbourUpdateListLocation):
        neighbour = _repo.get_neighbour(
            f'NEIGHBOUR#{data_in.id_address}',
            f'NEIGHBOUR#{data_in.id_address}')

    def search_address(data_in: _neighbour_schemas.NeighbourSearch):
        response = []
        list_id_address = []

        all_neighbours = _repo.get_all_neighbour()
        all_neighbour = sorted(
            all_neighbours, key=lambda d: d['NumberNeighbour'])
        if data_in.address:
            info_address_star = _repo.get_neighbour_star(
                f'SPACE#{data_in.id_star}',
                f'SPACE#{data_in.id_star}')
            star_point = next(
                item for item in all_neighbour if item["IdSpace"] == data_in.id_star)
            response.append(ast.literal_eval(info_address_star.get('Point')))
        else:
            info_address_star = _repo.get_neighbour_star(
                f'LOCATION#{data_in.id_star}',
                f'LOCATION#{data_in.id_star}')
            star_point = next(
                item for item in all_neighbour if item["IdSpace"] == info_address_star.get('OnIdAddress'))
            response.append(ast.literal_eval(
                info_address_star.get('PointAddress')))

        info_address_end = _repo.get_neighbour_star(
            f'LOCATION#{data_in.id_end}',
            f'LOCATION#{data_in.id_end}')
        print(info_address_end.get('OnIdAddress'))
        end_point = next(
            item for item in all_neighbour if item["IdSpace"] == info_address_end.get('OnIdAddress'))
       
        graph = _dfs.Graph(len(all_neighbours)+1, directed=False)
        for data in all_neighbours:
            point = int(data.get('NumberNeighbour'))
            list_end = data.get('ListAddressNeighbour')
            for item in list_end:
                graph.add_edge(point, int(item))
        traversal_path = graph.bfs(
            int(star_point.get('NumberNeighbour')),
            int(end_point.get('NumberNeighbour'))
        )
        graph.print_adj_list()
        print(traversal_path)
        # traversal_path = graph.dfs(
        #     int(star_point.get('NumberNeighbour')),
        #     int(end_point.get('NumberNeighbour'))
        # )
        # return traversal_path
        if traversal_path is None:
            traversal_path = graph.dfs(
                int(star_point.get('NumberNeighbour')),
                int(end_point.get('NumberNeighbour')))

        for data in traversal_path:
            test = next(
                item for item in all_neighbour if int(item["NumberNeighbour"]) == data)
            list_id_address.append(test.get('IdSpace'))

        list_id_address.pop(0)
        list_three_add = []
        _three_add = False
        script = 'Chạy đến '
        for data in list_id_address:
            info_address_ = _repo.get_neighbour_star(
                f'SPACE#{data}',
                f'SPACE#{data}')
            test = next(
                item for item in all_neighbour if item["IdSpace"] == data).get('ListAddressNeighbour')
            if len(test) < 2:  # check ngã 3 ngã tư
                script += info_address_.get('SpaceName') + ', '
                response.append(ast.literal_eval(info_address_.get('Point')))
            else:
                script += info_address_.get('SpaceName') + ','
                _three_add = True
                list_three_add.append(
                    ast.literal_eval(info_address_.get('Point')))
        # tip and mẹo
        # if list_id_address[0] > list_id_address[-1]:
            for index in range(len(response)-1):
                star = index
                # if index+1 > len(response):
                #     break
                end = index+1

                if not response[star][0] == response[end][-1]:
                    if not response[star][0] == response[end][0]:
                        response = response + list_three_add
                        print('ko lien thong')
                        break

        # response.pop()
        # test2 = ast.literal_eval(info_address_end.get('PointSpace'))
        # test = response[len(response)-1].append(test2)
        # print(test)
        # response.append()
        return {
            'Address': info_address_end.get('Address'),
            'ListAddress': response,
            'Script': script
        }
